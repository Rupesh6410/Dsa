class Solution:
    def findPages(self, arr, k):
        # code here
        if len(arr)<k:
            return -1
        
        def isTrue(k,mid):
            stud =1
            page=0
            for i in range(len(arr)):
                if page+arr[i]<=mid:
                    page+=arr[i]
                else:
                    stud+=1
                    page=arr[i]
                    if stud>k:
                        return False
            return True
        
        low=max(arr)
        high=sum(arr)
        ans=-1
        
        while low<=high:
            mid = (low+high)//2
            if isTrue(k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                
