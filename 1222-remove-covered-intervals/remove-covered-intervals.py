class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        prev=intervals[0]
        cnt=0
        end=0
        for i,j in intervals:
            if j>end:
                cnt+=1
                end=j
        return cnt



        