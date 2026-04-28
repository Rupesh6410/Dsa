class Solution:
    def segregate0and1(self, arr):
        # code here
        j = len(arr)-1
        i=0
        
        while i<j:
            if arr[i]==0:
                i+=1
            elif arr[j]==1:
                j-=1
            else:
                arr[i] ,  arr[j] =  arr[j] , arr[i]
                j-=1
                i+=1
                
                
        return arr