class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for s in strs:
            x = "".join(sorted(s))

            if x not in ans:
                ans[x] = []
            
            ans[x].append(s)

        return list(ans.values())
            
