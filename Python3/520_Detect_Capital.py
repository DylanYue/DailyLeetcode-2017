class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Very simple in Python...
        return word.isupper() or word.islower() or word.istitle()