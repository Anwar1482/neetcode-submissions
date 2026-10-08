class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area =0 
        l = 0
        r = len(heights)-1
        while l < r:
            if min(heights[l],heights[r])*abs(l-r)> max_area:
                max_area= min(heights[l],heights[r])*abs(l-r)
            if min(heights[l],heights[r]) == heights[r]:
                r-=1
            else:
                l+=1
        return max_area

        