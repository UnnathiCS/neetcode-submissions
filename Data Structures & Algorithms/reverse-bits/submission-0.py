class Solution:
    def reverseBits(self, n: int) -> int:
        s=format(n,'032b')
        rev_s=s[::-1]
        return int(rev_s,2)