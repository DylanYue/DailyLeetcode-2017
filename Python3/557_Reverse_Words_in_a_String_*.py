class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        revSentence=""
        for word in s.split():
            revSentence += self.reverseWord(word)
            revSentence += " "
        return revSentence.rstrip()
        
    def reverseWord(self, s):
        """
        This function reverses a single word.
        """
        revWord=""
        for i in range(len(s)):
            revWord += s[len(s)-1-i]
        return revWord
