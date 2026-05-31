class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        l=0
        cnt=0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            cnt=max(cnt,r-l+1)
        return cnt