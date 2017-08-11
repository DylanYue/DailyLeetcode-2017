class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        vals = (val for row in nums for val in row)
        return[[vals.next() for i in xrange(c)] for j in xrange(r)]