class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = Counter(nums)
        B = A.most_common(k)
        return [item[0] for item in B]