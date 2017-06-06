class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        i = 1
        while l[-i] == '' and i < len(l):
            i += 1
        return len(l[-i])
