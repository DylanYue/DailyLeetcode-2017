class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. sort the array (Ascending)
        # 2. Return the sum of the elements in step of 2
        return sum(sorted(nums)[::2])
