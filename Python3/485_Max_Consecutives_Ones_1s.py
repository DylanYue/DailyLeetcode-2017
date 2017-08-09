class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1st convert the list to a string
        # 2nd split the string by "0"
        # 3rd return the longest string length (among "1" strings)
        temp = ("".join(map(str, nums))).split('0')
        return max(map(len, temp))