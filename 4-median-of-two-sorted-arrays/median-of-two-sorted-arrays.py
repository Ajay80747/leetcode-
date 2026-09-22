class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1=nums1+nums2
        l=len(nums1)
        nums1.sort()
        if l%2==0:
            n=l//2
            k=((nums1[n]+nums1[n-1])/2)
            return k
        else:
            n=l//2
            k=nums1[n]
            return k


            
        