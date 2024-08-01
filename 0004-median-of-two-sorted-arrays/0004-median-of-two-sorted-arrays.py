class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sum=0
        nums3=nums1+nums2
        nums3.sort()
        if(len(nums3)%2!=0):
            sum=nums3[len(nums3)//2]
        else:
            sum=(nums3[len(nums3)//2]+nums3[(len(nums3)//2)-1])/2.0
        return sum

        