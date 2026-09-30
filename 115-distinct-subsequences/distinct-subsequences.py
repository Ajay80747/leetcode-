class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}

        def solve(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==t[j]:
                tk=solve(i+1,j+1)
                ntk=solve(i+1,j)
                dp[(i,j)]=tk+ntk
            else:
                dp[(i,j)]= solve(i+1,j)
            return  dp[(i,j)]
        return solve(0,0)
