class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp={}
        def rec(i,cnt):
            if i==len(nums):
                if cnt==target:
                    return 1
                return 0
            if (i,cnt) in dp:
                return dp[(i,cnt)]
            
            p=rec(i+1,cnt+nums[i])
            m=rec(i+1,cnt-nums[i])

            dp[(i,cnt)]=p+m
            return dp[(i,cnt)]
        return rec(0,0)
        
        