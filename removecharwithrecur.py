class Solution:
    def removeCharacter(self, s, c):
        # code here
        n=len(s)
        res=[]
        def rmv(s,c,i=0,n=n):
            if i==n:
                return ""
            if s[i]==c:
                return rmv(s,c,i+1,n)
            return s[i]+rmv(s,c,i+1,n)
        return rmv(s , c)
