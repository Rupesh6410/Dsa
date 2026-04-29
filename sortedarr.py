class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        for i in range(len(neg)):
            neg[i]=neg[i]**2
        for j in range(len(pos)):
            pos[j]=pos[j]**2
        
        neg.reverse()

        k=0
        l=0
        m = len(neg)
        n = len(pos)
        arr=[]

        while k<m and l<n:
            if neg[k]<pos[l]:
                arr.append(neg[k])
                k+=1
            else:
                arr.append(pos[l])
                l+=1
        while(l<n):
            arr.append(pos[l])
            l+=1
        while(k<m):
            arr.append(neg[k])
            k+=1
        return arr