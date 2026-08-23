class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])

        def isTrue(guess):
            count=0
            row=n-1
            col=0
            while row>=0  and col<m:
                if matrix[row][col]<=guess:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count

        low=matrix[0][0]
        high=matrix[n-1][m-1]

        res=-1

        while low<=high:
            guess=(low+high)//2
            ans = isTrue(guess)
            if ans<k:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res
             
