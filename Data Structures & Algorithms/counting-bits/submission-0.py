class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1): 
            s=bin(i)
            cnt=0
            for c in s:
                if c=='1':
                    cnt+=1
            res.append(cnt)
        return res
