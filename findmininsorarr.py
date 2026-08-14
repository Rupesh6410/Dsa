class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n = len(nums) 
        high = n-1
        ans = -1
        while low <= high:
            mid = (high+low)//2
            if nums[mid]>nums[n-1]:
                low = mid+1
            else:
                ans = nums[mid]
                high = mid-1
        return ans

