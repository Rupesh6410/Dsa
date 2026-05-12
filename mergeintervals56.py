class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a=[]
        intervals.sort()
        flag=True
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0] and flag:
                a.append(newInterval)
                flag=False
            a.append(intervals[i])
        if flag:
            a.append(newInterval)
        a.sort()
        res=[]
        st1=a[0][0]
        end1=a[0][1]
        for i in range(1, len(a)):
            st2=a[i][0]
            end2=a[i][1]
            if end1>=st2:
                st1=st1
                end1=max(end1,end2)
                continue
            res.append([st1,end1])
            st1=st2
            end1=end2
        res.append([st1,end1])
        return res
       