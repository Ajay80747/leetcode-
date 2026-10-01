class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp={}

        def solve(id):
            if id==len(s):
                return True
            if id in dp:
                return dp[id]
            for i in range(id+1,len(s)+1):
                w=s[id:i]
                if w in wordDict:
                    if solve(i):
                        dp[id]= True
                        return True
            dp[id]= False 
            return False
        return solve(0)



        

         

