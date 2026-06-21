class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        A = set(nums) 
        longest = 0
        for x in A: 
            if x-1 not in A:
                length =1
                while x+1 in A:
                    x = x+1
                    length = length +1
                longest = max(longest,length)
        return longest