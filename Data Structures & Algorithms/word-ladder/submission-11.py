class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque()
        q.append((beginWord, 1))
        while q:
            word, layer = q.popleft()
            step = False
            for i in range(len(word)):
                for c in letters:
                    temp = word[:i]
                    temp += c
                    if i+1<len(word):
                        temp +=word[i+1:]
                    if temp in wordSet:
                        q.append((temp, layer+1))
                        wordSet.remove(temp)
                        if temp==endWord:
                            return layer+1
        return 0