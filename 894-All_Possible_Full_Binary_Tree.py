

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res = []

        if N % 2 == 0:
            return []

        res.append([TreeNode()])

        i = 1
        while 2 * i + 1 <= N:
            temp = []
            j = 1
            while j < 2 * i:
                idx1 = j // 2
                idx2 = (2 * i - j) // 2
                temp.extend(self.merge(res[idx1], res[idx2]))
                j += 2
            res.append(temp)
            i += 1

        return res[N // 2]

    def merge(self, arr_lst1, arr_lst2):
        res = []

        n1 = len(arr_lst1)
        n2 = len(arr_lst2)

        for i in range(n1):
            for j in range(n2):
                res.append(self.construct_tree(arr_lst1[i], arr_lst2[j]))

        return res

    @staticmethod
    def construct_tree(tree_node1, tree_node2):
        root = TreeNode()
        root.left = tree_node1
        root.right = tree_node2

        return root
