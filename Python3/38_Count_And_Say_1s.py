class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        count = 1
        for i in range(n-1):
            count = 1
            resultList = []
            for j in range(0, len(s)-1):
                if s[j+1] == s[j]:
                    count += 1                    
                else:
                    resultList.append(str(count))
                    resultList.append(s[j])
                    count = 1
            resultList.append(str(count))
            resultList.append(s[-1])
            s = "".join(resultList)
        
        return s