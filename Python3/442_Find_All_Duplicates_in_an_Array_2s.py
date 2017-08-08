class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)):
            if nums[abs(nums[i])-1] < 0:
                result.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        return result