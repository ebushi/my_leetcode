import string
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        l = list(s)
        new_s = []
        str1 = ''

        while len(l) > 0:
            if len(l) == 1:
                new_s.append('1')
                new_s.append(l[0])
                l.pop(0)
            else:
                i = 1
                count = 1
                while i < len(l):
                    if l[0] == l[i]:
                        i += 1
                        count += 1
                        if i == len(l):
                            new_s.append(str(count))
                            new_s.append(l[0])
                          
                            for i in range(count):
                                l.pop(0)
                            return str1.join(new_s)
                    else:
                        new_s.append(str(count))
                        new_s.append(l[0])
                        
                        for i in range(count):
                            l.pop(0)
                        i = 1
                        count = 1
        return str1.join(new_s)
