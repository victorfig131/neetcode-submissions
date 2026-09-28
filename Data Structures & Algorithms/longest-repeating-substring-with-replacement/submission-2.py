class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==1: return 1
        l = 0
        r = 0
        total = 0
        count = {}
        maxFreq = 0

        while (r<len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            while(r-l+1 - maxFreq > k):
                count[s[l]]-=1
                l+=1
            
            total = max(total, r-l+1)
            r+=1

        return total