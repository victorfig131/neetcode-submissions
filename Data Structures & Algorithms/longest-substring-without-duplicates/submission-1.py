class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        if len(s) == 0: return 0

        l = 0
        r = 1
        longest = 0
        myset = set()
        myset.add(s[l])

        while(r<=len(s)):
            temp = r-l
            longest = max(temp, longest)
            if r == len(s):
                break
            if (s[r] not in myset):
                myset.add(s[r])
                r+=1
            elif (s[r] in myset):
                myset.remove(s[l])
                l+=1

        return longest
#zxyx

