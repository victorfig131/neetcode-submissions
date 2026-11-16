class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0

        while (i < len(nums) or j < len(nums)):
            while((j-i)<=k and j<len(nums)):
                if (nums[i] == nums[j]) and (i != j): return True
                j+=1
            i+=1
            j = i
        return False
