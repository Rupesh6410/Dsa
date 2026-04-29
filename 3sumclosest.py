class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        min_diff = float('inf')
        res = 0

        for i in range(n - 2):
            l = i + 1
            r = n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(total - target)

                
                if diff < min_diff:
                    min_diff = diff
                    res = total

                
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total  

        return res
            