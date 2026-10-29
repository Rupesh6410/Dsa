class Solution:
    def sumOfDigits(self, n):
        # code here
        def sum(n):
            if n==0:
                return 0
            ans=n%10
            n=n//10
            return ans+sum(n)
        return sum(n)
