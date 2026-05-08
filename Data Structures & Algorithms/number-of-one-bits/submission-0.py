class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)
        cnt=0
        for c in s:
            if c == '1':
                cnt+=1
        return cnt