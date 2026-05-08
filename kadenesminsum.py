class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        best=A[0]
        res=A[0]
        for i in range(1, len(A)):
            a=A[i]+best
            b=A[i]
            best=min(a,b)
            res=min(best,res)
        return res