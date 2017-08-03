class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1. pad the front and back of the grid with 0s and put them in an array of strings
        gridPadded = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        
        # 2. transpose the original grid
        gridTranspose = list(map(list, zip(*grid)))
        
        # 3. pad the transposed grid and add it to the first padded grid
        gridPadded += ['0' + ''.join(str(x) for x in row) + '0' for row in gridTranspose]
        
        # 4. count all the different value pairs e.g. "01", and "10". This number is the number of edges
        return sum(row.count('01') + row.count('10') for row in gridPadded)
