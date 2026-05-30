"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0,40),(5,10),(15,20)]
        # start=[0,5,15]
        # end =[10,20,40]
        # 0<10 yes
        # cnt=1,s=1
        # 5<10 yes -> cnt=2,s=2 reached while condn
        # res=2 ..
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        s=e=0
        res=cnt=0
        while s<len(intervals):
            if start[s]<end[e]:
                s+=1
                cnt+=1
            else:
                e+=1
                cnt-=1
            res=max(res,cnt)
        return res
