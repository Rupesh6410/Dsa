class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        n= len(nums)
        high = n-1
        while high>=low:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[n-1]:
                if nums[mid]<target:
                    low=mid+1
                else:
                    if target>=nums[0]:
                        high= mid-1
                    else:
                        low=mid+1
            if nums[mid]<=nums[n-1]:
                if nums[mid]>target:
                    high=mid-1
                else:
                    if target<=nums[n-1]:
                        low=mid+1
                    else:
                        high = mid-1
        return -1

        
