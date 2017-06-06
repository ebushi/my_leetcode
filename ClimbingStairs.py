class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = 0
        x = 0
        y = 0
        for x in range(n+1):
            for y in range(int(n/2)+1):
                if x + y*2 == n:
                    tmp = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
                    ways += tmp
        return int(ways)
       
