"""
Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. 

The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # This solution is not accepted by leetcode because of time limit.
        keys = []
        # sorts the list.
        nums.append(0)
        nums.sort()
        # determine the number of zeros in the list.
        neg_num = nums.index(0)
        neg = nums[0:neg_num]
        nums.reverse()
        posi_num = nums.index(0)
        posi = nums[0:posi_num]
        posi.sort()
        zero_num = len(nums) - posi_num - neg_num -1
        nums.sort()
        # more than three zeros.
        if zero_num >= 3:
            keys.append([0, 0, 0])
        elif zero_num > 0 and zero_num < 3:
            # search for (-n, 0, n) solutions.
            for i in neg:
                if -i in posi:
                    temp_key = [i, 0, -i]
                    temp_key.sort()
                    if temp_key not in keys:
                        keys.append(temp_key)
        # no zero solutions, the problem becomes a + b = -c.
        # case 1: two negative numbers and one positive number
        for i in posi:
            for j in neg:
                if (j != (-i-j) and (-i-j) in neg) or \
                   (j == (-i-j) and neg[neg.index(j)+1] == j):
                    temp_key = [j, -i-j, i]
                    temp_key.sort()
                    if temp_key not in keys:
                        keys.append(temp_key)

        # case 2: one negative number and two positive number
        for i in neg:
            for j in posi:
                if ((-i-j) in posi and j != (-i-j)) or \
                   (j == (-i-j) and posi[posi.index(j)+1] == j):
                    temp_key = [i, j, -i-j]
                    temp_key.sort()
                    if temp_key not in keys:
                        keys.append(temp_key)
        return keys

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Accepted by leetcode.
        keys = []
        if len(nums) < 3:
            return keys
        nums.sort()
        
        for i in range(0, len(nums)-2):
            if (i == 0 or nums[i] > nums[i-1]):
                negate = -nums[i]
                start = i + 1
                end = len(nums) - 1
                while (start < end):
                    # case 1
                    if nums[start] + nums[end] == negate:
                        temp_key = [nums[i], nums[start], nums[end]]
                        temp_key.sort()
                        keys.append(temp_key)
                        start += 1
                        end -= 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    # case 2
                    elif nums[start] + nums[end] < negate:
                        start += 1
                    else:
                        end -= 1
        return keys
