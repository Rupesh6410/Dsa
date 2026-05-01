class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        f = {}
        n = len(s)
        ans = 0
        
        while r < n:
            f[s[r]] = f.get(s[r], 0) + 1
            
            k = r - l + 1
            
            while k > len(f):
                f[s[l]] -= 1
                if f[s[l]] == 0:
                    del f[s[l]]
                l += 1
                k = r - l + 1   
            
            
            if k == len(f):
                ans = max(ans, k)
            
            r += 1
        
        return ans