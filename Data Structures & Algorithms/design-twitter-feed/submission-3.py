class Twitter:

    def __init__(self):
        self.follows = collections.defaultdict(set)
        self.posts = collections.defaultdict(collections.deque)   # newest first
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.time, tweetId))
        if len(self.posts[userId]) > 10:      # a feed never needs more than 10 per user
            self.posts[userId].pop()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for uid in self.follows[userId] | {userId}:   # include your own tweets
            if self.posts[uid]:
                t, tid = self.posts[uid][0]
                heap.append((-t, tid, uid, 0))        # -t: newest pops first
        heapq.heapify(heap)
        ans = []
        while heap and len(ans) < 10:
            _, tid, uid, i = heapq.heappop(heap)
            ans.append(tid)
            if i + 1 < len(self.posts[uid]):          # push that user's next-newest tweet
                t, nid = self.posts[uid][i + 1]
                heapq.heappush(heap, (-t, nid, uid, i + 1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)