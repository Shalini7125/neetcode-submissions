class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        minelement=float('inf')
        l,r=0,n-1
        while(l<=r):
            m=(r+l)//2
           
        
            if(nums[l]<=nums[m]):
                minelement=min(minelement,nums[l])
                l=m+1

                
            else:
                minelement=min(minelement,nums[m])
                r=m-1
        return minelement
              
      