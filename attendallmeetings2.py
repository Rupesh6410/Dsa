class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        i=0
        j=0
        m=len(start)
        n=len(end)
        ans=0
        room=0
        while i<m and j<n:
            if start[i]<end[j]:
                room+=1
                i+=1
                ans=max(room,ans)
            elif start[i]==end[j]:
                room-=1
                j+=1
                room+=1
                i+=1
            else:
                room-=1
                j+=1
        return ans
                