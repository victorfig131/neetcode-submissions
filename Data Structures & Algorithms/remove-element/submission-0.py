class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            k = 0
            j = 0
            max = 51
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[j] = nums[i]
                    j+=1
                    k+=1
                elif nums[i] == val:
                    nums[i] = max

            return k


