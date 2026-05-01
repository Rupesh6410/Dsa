class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        n=len(nums)
        res=10**18
        sum=0
        maxsum=0
        for i in range (n):
            maxsum+=nums[i]
        
        if maxsum<target:
            return 0
       

        while high<n:
            sum=sum+nums[high]
            while sum>=target:
                res=min(res , high-low+1)
                sum=sum-nums[low]
                low+=1
            high+=1
        return res
