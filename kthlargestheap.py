import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(0,k):
            heapq.heappush(heap , nums[i])
        for j in range(k , len(nums)):
            if heap[0]>nums[j]:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap , nums[j])
        return heap[0]
