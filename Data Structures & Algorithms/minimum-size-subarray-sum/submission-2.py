class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        smallest_length = 100001
        
        subarray = []
        while (r<len(nums) or sum(subarray)>=target):
            while(sum(subarray)>=target):
                smallest_length = min(smallest_length, len(subarray))
                subarray.pop(0)
            if(r<len(nums)):
                subarray.append(nums[r])
                r+=1

        if(smallest_length == 100001): return 0
        return smallest_length
