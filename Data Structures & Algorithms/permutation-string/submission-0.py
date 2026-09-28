class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = {}
        window = {}

        for ch in s1:
            s1count[ch] = s1count.get(ch, 0) + 1

        l = 0
        for r in range(len(s2)):
            ch = s2[r]

            # Add current char to window
            window[ch] = window.get(ch, 0) + 1

            # If window gets too big, shrink from left
            if r - l + 1 > len(s1):
                left_char = s2[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l += 1

            # If window size matches s1, compare dictionaries
            if r - l + 1 == len(s1):
                if window == s1count:
                    return True

        return False
