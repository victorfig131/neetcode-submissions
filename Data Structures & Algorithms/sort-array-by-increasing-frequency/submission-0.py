class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict = {}
        result = []*len(nums)
        for i in nums:
            dict[i] = dict.get(i,0) + 1

        ordered = sorted(dict,key= lambda x: (dict[x], -x))


        for i in ordered:
            for j in range(dict[i]):
                result.append(i)

        return result

