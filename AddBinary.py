class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = list(a)
        lb = list(b)
        
        bin_a = 0
        i = 0
        while i < len(la):
            bin_a += int(la[-i - 1]) * 2 ** i
            i += 1
        
        bin_b = 0
        j = 0
        while j < len(lb):
            bin_b += int(lb[-j - 1]) * 2 ** j
            j += 1
        
        result = list(bin(bin_a + bin_b))
        
        return str(''.join(result[2:]))

