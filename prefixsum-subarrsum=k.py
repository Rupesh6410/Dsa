class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        f={}
        f[0]=1
        ans=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in f:
                ans+=f[sum-k]

            if sum in f:
                f[sum]+=1
            else:
                f[sum]=1
        return ans
