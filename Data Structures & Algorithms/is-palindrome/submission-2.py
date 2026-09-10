class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        l = 0
        r = len(s)-1

        for l in range(len(s)//2):
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True