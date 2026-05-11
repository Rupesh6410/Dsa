class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one = 0
        zero = 0
        res = 0

        f = {}
        f[0] = -1

        for i in range(len(nums)):

            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            if diff in f:
                res = max(res, i - f[diff])
            else:
                f[diff] = i

        return res
        