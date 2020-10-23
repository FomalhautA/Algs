class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return '0'

        Q, R = divmod(K, 2)
        letter = self.kthGrammar(N - 1, Q+R)

        if letter == '0':
            return '1' if R == 0 else '0'

        if letter == '1':
            return '0' if R == 0 else '1'


if __name__ == '__main__':
    s = Solution()
    re = s.kthGrammar(4, 4)
    print(re)