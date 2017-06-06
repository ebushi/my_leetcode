class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            if int(str(x)[::-1]) > 2**31:
                return 0
            else:
                return int(str(x)[::-1])
        else:
            x_tmp = abs(x)
            if int(str(x_tmp)[::-1]) > 2**31:
                return 0
            else:
                return int('-' + (str(x_tmp)[::-1]))
