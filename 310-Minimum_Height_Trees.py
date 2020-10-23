from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        degree = [0] * n
        outer = defaultdict(list)

        for edge in edges:
            a, b = edge
            degree[a] += 1
            degree[b] += 1

            outer[a].append(b)
            outer[b].append(a)

        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        ans = None
        while len(leaves) >= 2:
            if len(leaves) == 2:
                ans = leaves

            next_leaves = []
            for a in leaves:
                for node in outer[a]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        next_leaves.append(node)
            leaves = next_leaves

        return leaves if leaves else ans


if __name__ == '__main__':
    s = Solution()
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    res = s.findMinHeightTrees(n, edges)
    print(res)
