import collections


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        graph = [i for i in range(n)]
        sizes = [1 for i in range(n)]

        def find(x):
            while graph[x] != x:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return x

        def union(x, y):
            x1, y1 = find(x), find(y)
            if x1 != y1:
                if sizes[x1] <= sizes[y1]:
                    graph[x1] = y1
                    sizes[y1] += sizes[x1]
                else:
                    graph[y1] = x1
                    sizes[x1] += sizes[y1]

        for x, y in pairs:
            union(x, y)

        groups = collections.defaultdict(list)
        for i in range(n):
            i1 = find(i)
            groups[i1].append(i)

        res = [s[i] for i in range(n)]
        for group in groups.values():
            substr = sorted([s[i] for i in group])
            idxs = sorted(group)
            for i in range(len(group)):
                res[idxs[i]] = substr[i]

        return res


if __name__ == '__main__':
    s = Solution()
    source = "dcab"
    pairs = [[0, 3], [1, 2]]
    res = s.smallestStringWithSwaps(source, pairs)
    print(res)
