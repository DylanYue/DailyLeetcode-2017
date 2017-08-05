class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(0, len(s)-1):
            tempString = s[:i]
            if s[i] == "+" and s[i+1] == "+":
                tempString += "--"
                tempString += s[i+2:]
                result.append(tempString)
        return result
