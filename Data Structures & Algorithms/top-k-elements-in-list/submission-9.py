class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        output = []
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        
        sortDict = sorted(dict.keys(), key=dict.get, reverse=True)

        for i in range(k):
            output.append(sortDict[i])

        return output