class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        l = 0
        r = len(height)-1
        maxL = 0
        maxR = 0
        total = 0

        while (l < r):
            if (height[l]<=height[r]):
                maxL = max(maxL, height[l])
                water = maxL - height[l]
                total += water
                l+=1
            else:
                maxR = max(maxR, height[r])
                water = maxR - height[r]
                total += water
                r-=1
            
        return total


