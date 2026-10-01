class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}

        def sol(i,j):
            if j==len(word2):
                return len(word1)-i
            if  i==len(word1):
                return len(word2)-j 
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i]==word2[j]:
                dp[(i,j)]= sol(i+1,j+1)
                return dp[(i,j)]
            h=sol(i+1,j)
            k=sol(i+1,j+1) 
            m=sol(i,j+1)
            
            dp[(i,j)]= 1+ min(h,k,m)
            return dp[(i,j)]
        return sol(0,0)

        