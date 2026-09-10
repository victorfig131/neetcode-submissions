class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dict = {}
        tempres=1
        res = 1

        for i in nums:
            dict[i] = i

        for i in nums:
            tempres = 1
            while(i + 1 in dict):
                tempres+=1
                i+=1
            if tempres > res:
                res = tempres
        
        return res


