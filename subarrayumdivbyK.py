class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum=0
        ans=0
        res=0
        f={}
        f[0]=1
        for i in range(len(nums)):
            sum+=nums[i]
            res=sum%k
            if res in f:
                ans+=f[res]
                f[res]+=1
            else:
                f[res]=1
        return ans

