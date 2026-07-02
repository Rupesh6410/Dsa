class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for word in s:
            f[word]= f.get(word ,0)+1
        
        for i in range(len(s)):
            if f.get(s[i])==1:
                return i 
            

        return -1
        
