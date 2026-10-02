class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words)==1:
            return words[0]
        graph = collections.defaultdict(set)
        indeg = collections.defaultdict(int)
        alphabet = set()
        for ch in words[0]:
            alphabet.add(ch)
        for idx in range(len(words)-1):
            first = words[idx]
            second = words[idx+1]
            for ch in second:
                alphabet.add(ch)
            length = min(len(first), len(second))
            modified = False
            for i in range(length):
                if first[i]!=second[i]:
                    modified = True
                    if second[i] not in graph[first[i]]:
                        indeg[second[i]]+=1
                    graph[first[i]].add(second[i])
                    break
            if len(first)>len(second) and not modified:
                return ""
        print(graph)
        print(indeg)
        print(alphabet)
        q = deque()
        for ch in alphabet:
            if ch not in indeg:
                q.append(ch)
        ans = ""
        while q:
            ch = q.popleft()
            ans += ch
            for nei in graph[ch]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    del indeg[nei]
                    q.append(nei)
        print(ans)
        return ans if len(ans)==len(alphabet) else ""