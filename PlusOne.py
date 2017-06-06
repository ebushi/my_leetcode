class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = 0

        for i in range(len(digits)):
            n = n + digits[-i-1] * 10**i

        n = n + 1
        list_n = list(str(n))

        for index, item in enumerate(list_n):
            list_n[index] = int(item)

        return list_n
