class Solution(object):
    def countSubstrings(self, s):
        """
        Manacher Algorithm
        :type s: str
        :rtype: int
        """
        A = '@#' + '#'.join(s) + '#$'
        Z = [0] * len(A)

        center = right = 0

        for i in range(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]

        return sum([(v + 1) / 2 for v in Z])
