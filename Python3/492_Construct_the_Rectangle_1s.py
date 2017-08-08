class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        SQRT = int(math.sqrt(area))
        while SQRT > 0:
            if area % SQRT == 0:
                return [area/SQRT, SQRT]
            else:
                SQRT -= 1