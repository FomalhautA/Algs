import collections


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node) for node in range(1, N + 1) if node not in color)


if __name__ == '__main__':
    s = Solution()
    dis = [[1, 2], [3, 4], [4, 5], [3, 5]]

    ans = s.possibleBipartition(5, dislikes=dis)
    print(ans)
