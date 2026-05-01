class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        res=-10**18
        sum=0
        for i in range(k):
            sum=sum+arr[i]
        
        n=len(arr)
        low=0
        high=k-1
        while high<n:
            res=max(res, sum)
            low+=1
            high+=1
            if high==n:
                break
            sum=sum+arr[high]-arr[low-1]
        
        return res
            
        