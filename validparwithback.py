class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def gp(n,open=0, close=0,temp="",ans=ans):
            if open==n and close==n:
                ans.append(temp)
                return ans
            if open<n:
                temp+="("
                gp(n,open+1,close,temp,ans)
                temp=temp[:-1]
            if open>close:
                temp+=")"
                gp(n,open , close+1,temp,ans)
                temp=temp[:-1]
            return ans
        return gp(n)
