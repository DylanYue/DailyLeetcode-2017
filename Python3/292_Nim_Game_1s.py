class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # If you encounter 4k when you need to draw, then you lose. Otherwise, you win.
        return True if n % 4 != 0 else False