class Solution:
    def fib(self, n: int) -> int:
        def fibb(n):
            if n==0:
                return 0
            if n==1:
                return 1
            ans1=fibb(n-1)
            ans2=fibb(n-2)
            ans= ans1+ans2    
            return ans
        return fibb(n)
