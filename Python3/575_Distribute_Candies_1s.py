class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 1. Convert candies to a set
        # 2. Get the length of the set
        # 3. If length <= half of candies length, retun length of set
        #    else: return half of candies length
        
        candySet = set(candies)
        if len(candySet) <= len(candies)/2:
            return len(candySet)
        else:
            return len(candies)/2
