import heapq 
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        max_heap=[]
        for x in arr:
            heapq.heappush(max_heap , -x)
            if len(max_heap)>k:
                heapq.heappop(max_heap)
            
        return -max_heap[0]
                
            
