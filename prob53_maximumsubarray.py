"""
Find the contiguous subarray within an array (containing 
at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)

    def maxSubArray2(self, nums):
        # Divide and conquer method.
        return self.maximumSubArray(nums, 0, len(nums)-1)[-1]
    
    def maximumSubArray(self, nums, low, high):
        if high == low:
            return (low, high, nums[low])
        else:
            mid = (low + high) / 2
            (leftLow, leftHigh, leftSum) = self.maximumSubArray(nums, low, mid)
            (rightLow, rightHigh, rightSum) = \
                self.maximumSubArray(nums, mid+1, high)
            (crossLow, crossHigh, crossSum) = \
                self.maxCrossingSubArray(nums, low, mid, high)
            if leftSum >= rightSum and leftSum >= crossSum:
                return (leftLow, leftHigh, leftSum)
            elif rightSum >= leftSum and rightSum >= crossSum:
                return (rightLow, rightHigh, rightSum)
            else:
                return (crossLow, crossHigh, crossSum)

    def maxCrossingSubArray(self, nums, low, mid, high):
        leftSum = -float('inf')
        tempSum = 0
        for i in range(mid, low-1, -1):
            tempSum += nums[i]
            if tempSum > leftSum:
                leftSum = tempSum
                leftMax = i
        rightSum = -float('inf')
        tempSum = 0
        for i in range(mid+1, high+1):
            tempSum += nums[i]
            if tempSum > rightSum:
                rightSum = tempSum
                rightMax = i
        return (leftMax, rightMax, leftSum + rightSum)
            
