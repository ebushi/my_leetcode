class Solution(object):
    def isValid(self, s):
        def filte(s):
            if s == '(' or s == ')' or s == '[' or s == ']' or s == '{' or s == '}':
                return True
            else:
                return False

        filted_s = list(filter(filte, s))

        print(filted_s)

        s1 = []

        while len(filted_s) != 0:
            if filted_s[0] == '{' or filted_s[0] == '[' or filted_s[0] == '(':
                s1.append(filted_s.pop(0))
            else:
                if len(s1) == 0:
                    return False
                else:
                    if filted_s[0] == '}':
                        if s1[-1] == '{':
                            s1.pop()
                            filted_s.pop(0)
                            continue
                        else:
                            return False

                    if filted_s[0] == ']':
                        if s1[-1] == '[':
                            s1.pop()
                            filted_s.pop(0)
                            continue
                        else:
                            return False

                    if filted_s[0] == ')':
                        if s1[-1] == '(':
                            s1.pop()
                            filted_s.pop(0)
                            continue
                        else:
                            return False
        if len(s1) != 0:
            return False
        else:
            return True
