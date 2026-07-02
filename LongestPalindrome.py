class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        
       
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        res = 0
        odd = False
        
        for count in freq.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                odd = True
        
 
        if odd:
            res += 1
        
        return res
