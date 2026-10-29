class Solution:
    def isSorted(self, arr):
        # code here
        n=len(arr)
        def check(arr,i=0,n=n):
            if  i==n-1:
                return True
            if arr[i]>arr[i+1]:
                return False
            return check(arr,i+1,n)
        return check(arr)
            
        
