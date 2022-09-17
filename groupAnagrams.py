class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagramMaps = []
        
        for s in strs:
            strMap = {}
            for c in s:
                strMap[c] = 1 + strMap.get(c, 0)
            try:
                i = anagramMaps.index(strMap)
                answer[i].append(s)
            except ValueError:
                answer.append([s])
                anagramMaps.append(strMap)
        
        return answer

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
