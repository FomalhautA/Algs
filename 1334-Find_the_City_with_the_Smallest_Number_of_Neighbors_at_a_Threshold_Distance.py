import copy
import numpy as np


class Solution(object):
    def findTheCity_Floyd_Wallshall(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        minum = 100
        city = -1

        dist = self.init_dist(n, edges)

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[j][i] = dist[i][j]

        for i in range(n):
            count = len(list(filter(lambda x: x <= distanceThreshold, dist[i])))
            if count <= minum:
                minum = count
                city = i

        return city

    def findTheCity_Dijkstra(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        minum = 100
        city = -1

        dist_ori = self.init_dist(n, edges)

        for start in range(n):
            dist = copy.deepcopy(dist_ori)
            shortPath = np.Inf * np.ones(n)
            visited = np.zeros(n)

            shortPath[start] = 0
            visited[start] = 1

            for count in range(n - 1):
                shortest = np.Inf
                pick = -1
                for i in range(n):
                    if visited[i] == 0 and dist[start][i] < shortest:
                        shortest = dist[start][i]
                        pick = i

                shortPath[pick] = shortest
                visited[pick] = 1

                for i in range(n):
                    if visited[i] == 0 and dist[start][pick] + dist[pick][i] < dist[start][i]:
                        dist[start][i] = dist[start][pick] + dist[pick][i]
                        dist[i][start] = dist[start][i]

            reachable = len(list(filter(lambda x: x <= distanceThreshold, shortPath)))
            if reachable <= minum:
                minum = reachable
                city = start

        return city

    @staticmethod
    def init_dist(n, edges):
        dist = np.Inf * np.ones((n, n))
        for i in range(n):
            dist[i][i] = 0

        for edge in edges:
            i = edge[0]
            j = edge[1]
            dist[i][j] = edge[2]
            dist[j][i] = edge[2]

        return dist


if __name__ == '__main__':
    a = Solution()
    n = 5
    distanceThreshold = 2
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]

    city = a.findTheCity_Dijkstra(n, edges, distanceThreshold)
    print(city)
