class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=""
        for c in s:
            if ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") or ord("0")<=ord(c)<=ord("9"):
                newStr+=c.lower()
        return newStr==newStr[::-1]