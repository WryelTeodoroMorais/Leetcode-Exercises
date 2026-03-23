class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        result1 = sorted(nums3)

        if len(result1) % 2 == 1:
            result2 = float(result1[len(result1)//2])
        else:
            result2 = float((result1[len(result1)//2] + result1[len(result1)//2-1])/2)
        return result2 
        