import collections


class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)

        graph = [item for item in range(n)]

        def find(x):
            while graph[x] != x:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return x

        def union(x, y):
            x1, y1 = find(x), find(y)
            graph[x1] = y1

        for x, y in allowedSwaps:
            union(x, y)

        groups = collections.defaultdict(list)
        for i in range(n):
            i1 = find(i)
            groups[i1].append(i)

        res = 0
        for ids in groups.values():
            counter = collections.Counter()
            for idx in ids:
                counter[source[idx]] += 1
                counter[target[idx]] -= 1
            res += sum(abs(val) for val in counter.values()) / 2

        return res


if __name__ == '__main__':
    s = Solution()
    source = [50, 46, 54, 35, 18, 42, 26, 72, 75, 47, 50, 4, 54, 21, 18, 18, 61, 64, 100, 14]
    target = [83, 34, 43, 73, 61, 94, 10, 68, 74, 31, 54, 46, 28, 60, 18, 18, 4, 44, 79, 92]
    allowedSwaps = [[1, 8], [14, 17], [3, 1], [17, 10], [18, 2], [7, 12], [11, 3], [1, 15], [13, 17], [18, 19], [0, 10], [15, 19],
     [0, 15], [6, 7], [7, 15], [19, 4], [7, 16], [14, 18], [8, 10], [17, 0], [2, 13], [14, 10], [12, 17], [2, 9],
     [6, 15], [16, 18], [2, 16], [2, 6], [4, 5], [17, 5], [10, 13], [7, 2], [9, 16], [15, 5], [0, 5], [8, 0], [11, 12],
     [9, 7], [1, 0], [11, 17], [4, 6], [5, 7], [19, 12], [3, 18], [19, 1], [13, 18], [19, 6], [13, 6], [6, 1], [4, 2]]
    res = s.minimumHammingDistance(source, target, allowedSwaps)
    print(res)
