class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        count = {}
        against = {}

        for char in s1:
            against[char] = against.get(char, 0) + 1

        l = 0
        while l < k:
            char = s2[l]
            count[char] = count.get(char, 0) + 1
            l += 1

        if count == against:
            return True

        l = 0
        r = k
        while r < len(s2):
            outgoing = s2[l]
            count[outgoing] -= 1
            if count[outgoing] == 0:
                del count[outgoing]

            incoming = s2[r]
            count[incoming] = count.get(incoming, 0) + 1

            if count == against:
                return True

            l += 1
            r += 1

        return False