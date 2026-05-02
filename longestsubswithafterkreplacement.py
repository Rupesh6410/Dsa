class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        f = {}
        max_freq=0
        ans = 0

        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            max_freq=max(max_freq,f[s[r]])

            while r-l+1-max_freq>k:
                f[s[l]]-=1
                if f[s[l]]==0:
                    del[f[s[l]]]
                l+=1
            ans=max(ans,r-l+1)
        return ans