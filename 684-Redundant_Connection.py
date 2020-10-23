# Disjoint Set


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        class DSU(object):
            def __init__(self):
                self.par = range(1001)
                self.rnk = [0] * 1001

            def find(self, x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])

                return self.par[x]

            def union(self, x, y):
                xr, yr = self.find(x), self.find(y)
                if xr == yr:
                    return False
                elif self.rnk[xr] < self.rnk[yr]:
                    self.par[xr] = yr
                elif self.rnk[xr] > self.rnk[yr]:
                    self.par[yr] = xr
                else:
                    self.par[yr] = xr
                    self.rnk[xr] += 1

                return True

        dsu = DSU()
        for edge in edges:
            x, y = edge
            if not dsu.union(x, y):
                return edge
