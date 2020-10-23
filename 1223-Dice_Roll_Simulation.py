class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        mems = dict()
        modulo = 10**9 + 7

        def dieRoll(n, last, consec):
            if (n, last, consec) in mems:
                return mems[(n, last, consec)]

            if n == 0:
                return 1

            res = 0
            for i in range(1, len(rollMax)+1):
                if i == last:
                    if consec < rollMax[i-1]:
                        res += dieRoll(n-1, last=i, consec=consec+1)
                else:
                    res += dieRoll(n-1, last=i, consec=1)

            mems[(n, last, consec)] = res % modulo

            return mems[(n, last, consec)]

        return dieRoll(n, last=0, consec=0) % modulo


if __name__ == '__main__':
    solu = Solution()
    rollMax = [1, 1, 1, 2, 2, 3]
    res = solu.dieSimulator(3, rollMax)
    print(res)
