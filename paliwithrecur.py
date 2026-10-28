class Solution:
    def isPalindrome(self, s):
        # code here
        length=len(s)-1
        def pali(s, low=0 , high=length):
            
            n=high-low+1
            if n==0 or n==1:
                return True
            
            if s[low]!=s[high]:
                return False
            
            return pali(s, low+1 , high-1)
        return pali(s)
