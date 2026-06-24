import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        h3=list(heapq.merge(nums1,nums2))
        n=len(h3)
        l,r=0,n-1
        m=(l+r)//2
        if(n%2==0):
            return (h3[m]+h3[m+1])/2
        else:
            return h3[m]

        