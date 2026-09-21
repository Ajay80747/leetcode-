class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        lo=0
        for i in nums:
            if i-1 not in nums:
                le=1
                while i+le in nums:
                    le+=1
                lo=max(lo,le)
        return lo




        