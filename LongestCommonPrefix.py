class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # is empty
        if len(strs) == 0:
            return ''
        # find the shortest string in strs
        str_len = []
        for l in range(len(strs)):
            str_len.append(len(strs[l]))
        min_str_len = min(str_len)
        i = 0
        while i < min_str_len:
            j = 1
            while j < len(strs):
                if strs[0][i] == strs[j][i]:
                    j += 1
                else:
                    return strs[0][0:i]
            i += 1
        return strs[0][0:i]
