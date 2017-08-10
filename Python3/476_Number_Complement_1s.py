class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Bit left shift 1 until it is one digit bigger than num 
        i = 1
        while i <= num:
            i = i << 1
        # do a bitwise xor using "1111" and num
        return (i-1) ^ num