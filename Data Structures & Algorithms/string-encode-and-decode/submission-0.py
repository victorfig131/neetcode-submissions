class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for s in strs:
            encodedS = encodedS + s + "@" + str(len(s)) + "#"
        return encodedS
    def decode(self, s: str) -> List[str]:
        result = []
        strStart = 0
        for i, c in enumerate(s):
            j=i
            if c == "@" and s[i+1].isdigit():
                while s[j] != "#":
                    j+=1
                strlen = int(s[i+1:j])
                newStr = s[strStart:strStart+strlen]
                result.append(newStr)
                strStart = j+1
        return result
