class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0

        seen = set()

        while j < len(nums):
            while (j-i)>k:
                seen.remove(nums[i])
                i+=1
            if (nums[j] in seen):
                return True
            seen.add(nums[j])
            j+=1
        return False
