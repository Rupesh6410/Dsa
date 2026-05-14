class Solution:
    def isIntersect(self, intervals):
       # Code Here
       intervals.sort()
       st1=intervals[0][0]
       end1=intervals[0][1]
       for i in range(1 ,len(intervals)):
           st2=intervals[i][0]
           end2=intervals[i][1]
           
           if end1>=st2:
               return True
           st1=st1
           end1=max(end1,end2)
       return False
           