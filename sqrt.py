
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        m = 0
        n = x
        while n - m >= 0.0001:
            if ((m + n)/2)**2 - x <= 0:
                m = (m + n)/2
            else:
                n = (m + n)/2
        return m

x = 121

sol = Solution()

print(sol.mySqrt(x))
