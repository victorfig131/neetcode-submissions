class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dict = {}
        sortedS = []

        for i in (strs):
            chars = [0]*26
            for j in i:
                chars[ord(j)-ord('a')] +=1  

            chars = tuple(chars)
            if(chars in dict):
                dict[chars].append(i)  
            else:
                dict[chars] = [i]

            #sortedS[i] = "".join(sorted(strs[i]))

        resdict = {}
        for key, value in dict.items():
            newKey = tuple(value)
            if newKey in resdict:
                resdict[newKey].append(key)
            else:
                resdict[newKey] = [key]

        for key in dict:
            res.append(dict[key])

        return res


        
        

        





        