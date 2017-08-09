class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # For this question, we just need to count the number of "1" bits and make it the same as the input
        return ["%d:%02d" % (h, m) 
               for h in range(12) for m in range(60)
               if (bin(h) + bin(m)).count('1') == num]