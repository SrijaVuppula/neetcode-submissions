class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = defaultdict(list)
        
        for x in strs:
            key = tuple(sorted(x))
            A[key].append(x)

        return list(A.values())