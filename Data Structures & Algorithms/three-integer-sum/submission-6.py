class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # skip duplicate i values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # two pointers
            l = i + 1
            r = n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # move both pointers
                    l += 1
                    r -= 1

                    # skip duplicate l
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    # skip duplicate r
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res
