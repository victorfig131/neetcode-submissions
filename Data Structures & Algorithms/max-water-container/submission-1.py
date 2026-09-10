class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r= len(heights)-1
        maxArea = min(heights[l],heights[r])*(r-l)

        while(l<r):
            maxArea = max(maxArea, min(heights[l],heights[r])*(r-l))
            if (heights[r]>heights[l]):
                l+=1
            else:
                r-=1
            
        return maxArea