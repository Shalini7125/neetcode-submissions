class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        volume=0
        while(left<right):
            volume=max(volume,(right-left)*min(heights[left],heights[right]))
            if(heights[left]>heights[right]):
                right-=1
            else:
                left+=1
        return volume

        