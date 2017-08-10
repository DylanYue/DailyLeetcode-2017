class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            if (i % 3) and (i % 5):
                result.append(str(i))
            elif (not i % 3) and (i % 5):
                result.append('Fizz')
            elif (i % 3) and (not i % 5):
                result.append('Buzz')
            else:
                result.append('FizzBuzz')
        return result