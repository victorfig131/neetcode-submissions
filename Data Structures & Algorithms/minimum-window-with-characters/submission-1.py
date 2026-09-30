class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        l = 0
        best_len = float('inf')
        best = ""

        for r, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                # update best
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best = s[l:r+1]

                # shrink
                left_char = s[l]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        return best
