class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Use a variable to record the postion of 0
        zeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i]
                zeroIndex += 1