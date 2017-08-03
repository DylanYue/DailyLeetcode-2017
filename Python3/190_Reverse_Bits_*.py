class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        initBin = '{0:032b}'.format(n)
        revBin = initBin[::-1]
        return(int(revBin, 2))
