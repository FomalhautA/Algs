import queue


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        else:
            return self.core(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def core(self, root, sum):
        path_cn = 0

        if root is None:
            return path_cn

        if root.val == sum:
            path_cn += 1

        path_cn += self.core(root.left, sum - root.val)
        path_cn += self.core(root.right, sum - root.val)

        return path_cn


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.tag = 0


class BST(object):
    def __init__(self):
        self.root = None

    def constructor(self, lst):
        self.root = TreeNode(lst[0])
        for i in range(1, len(lst)):
            node = TreeNode(lst[i])
            self.insert(node)

    def insert(self, node):
        p = self.root
        while p:
            if node.value < p.value:
                if not p.left:
                    p.left = node
                    break
                else:
                    p = p.left
            else:
                if not p.right:
                    p.right = node
                    break
                else:
                    p = p.right

    def remove(self, data, node):
        if not data:
            return node

        if data < node.value:
            node.left = self.remove(data, node.left)
        elif data > node.value:
            node.right = self.remove(data, node.right)
        else:
            if node.left and node.right:
                node.value = self.find_min(node.right).value
                node.right = self.remove(node.value, node.right)
            else:
                node = node.left if node.left else node.right

    def find_min(self, node):
        if not node:
            return node

        if node.left:
            return self.find_min(node.left)
        else:
            return node

    def preOrder(self, node):
        if not node:
            return

        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def middleOrder(self, node):
        if not node:
            return

        self.middleOrder(node.left)
        print(node.value)
        self.middleOrder(node.right)

    def rearOrder(self, node):
        if not node:
            return

        self.rearOrder(node.left)
        self.rearOrder(node.right)
        print(node.value)

    def preOrder2(self, node):
        stack = []
        stack.append(node)

        while stack:
            p = stack.pop()
            while p:
                print(p.value)
                stack.append(p.right)
                p = p.left

    def middleOrder2(self, node):
        stack = []
        p = node
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                print(p.value)
                p = p.right

    def rearOrder2(self, node):
        stack = []

        p = node
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()

            if p.tag == 0:
                p.tag = 1
                stack.append(p)
                p = p.right
            else:
                print(p.value)
                p = None

    def BFS(self, node):
        que = queue.Queue()
        que.put(node)
        while not que.empty():
            a = que.get()
            print(a.value)
            if a.left:
                que.put(a.left)
            if a.right:
                que.put(a.right)


if __name__ == '__main__':
    a = [1, 3, 2, 4, 6, 12, 8, 15, 10, 5, 9, 7, 13, 11, 14]
    bst = BST()
    bst.constructor(a)
    node = TreeNode(6.5)
    bst.insert(node)
    bst.middleOrder(bst.root)
    # bst.preOrder(bst.root)
    print('--------------------------')
    # bst.middleOrder(bst.root)
    print('--------------------------')
    # bst.rearOrder(bst.root)
    # bst.preOrder2(bst.root)
    # bst.middleOrder2(bst.root)
    # bst.BFS(bst.root)


