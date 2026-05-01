class Solution:
    def longestKSubstr(self, s, k):
        # code here
        l=0
        r=0
        n=len(s)
        f={}
        res=-1
        while r<n:
            f[s[r]]=f.get(s[r],0)+1
            while len(f)>k:
                f[s[l]]-=1
                if f[s[l]]==0:
                    del f[s[l]]
                l+=1
            if len(f)==k:
                res=max(res , r-l+1)
            
            r+=1
        return res
            
                
        
        