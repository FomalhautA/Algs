
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)

        if l % 2 == 1:
            return False

        temp = []
        for i in range(l):
            if s[i] in ['(', '[', '{']:
                temp.append(s[i])
            else:
                if len(temp) == 0:
                    return False
                if self.ispair(temp[-1], s[i]):
                    del (temp[-1])
                else:
                    return False

        if len(temp) == 0:
            return True

    def ispair(self, a, b):
        if (a, b) in [('(', ')'), ('[', ']'), ('{', '}')]:
            return True
        else:
            return False
