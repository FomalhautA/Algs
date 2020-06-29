
class AVL_Node(object):
    def __init__(self, data):
        self.data = data
        self.depth = 1
        self.balance = 0
        self.left = None
        self.right = None
        self.parent = None


class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def constructor(self, lst):
        if not lst:
            return

        for item in lst:
            self.insert(self.root, item)

    def insert(self, node, data):
        new_node = AVL_Node(data)
        if not node:
            self.root = new_node
            return
        if data < node.data:
            if node.left:
                self.insert(node.left, data)
            else:
                node.left = new_node
                new_node.parent = node
        else:
            if node.right:
                self.insert(node.right, data)
            else:
                node.right = new_node
                new_node.parent = node

        node.depth = self.calc_depth(node)
        node.balance = self.calc_balance(node)

        self.rebalance(node)

    def remove(self, node, data):
        if not node:
            return

        if node.data > data:
            self.remove(node.left, data)
        elif node.data < data:
            self.remove(node.right, data)
        else:
            if node.left and node.right:
                node.data = self.find_min(node.right).data
                self.remove(node.right, node.data)
            else:
                parent = node.parent
                child = node.left if node.left else node.right
                if child:
                    child.parent = parent

                if parent:
                    if node == parent.left:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    self.root = child
                node = None

        if node:
            node.depth = self.calc_depth(node)
            node.balance = self.calc_balance(node)
            self.rebalance(node)

    def rebalance(self, node):
        if node.balance >= 2:
            if node.left.balance == -1:
                self.left_rotate(node.left)
            self.right_rotate(node)

        if node.balance <= -2:
            if node.right.balance == 1:
                self.right_rotate(node.right)
            self.left_rotate(node)

    def find_min(self, node):
        if not node:
            return node

        if node.left:
            return self.find_min(node.left)
        else:
            return node

    def right_rotate(self, node):
        parent = node.parent
        left_son = node.left
        right_grandson = left_son.right

        left_son.parent = parent
        if parent:
            if node == parent.left:
                parent.left = left_son
            else:
                parent.right = left_son
        else:
            self.root = left_son

        left_son.right = node
        node.parent = left_son

        node.left = right_grandson
        if right_grandson:
            right_grandson.parent = node

        node.depth = self.calc_depth(node)
        node.balance = self.calc_balance(node)
        left_son.depth = self.calc_depth(left_son)
        left_son.balance = self.calc_balance(left_son)

    def left_rotate(self, node):
        parent = node.parent
        right_son = node.right
        left_grandson = right_son.left

        right_son.parent = parent
        if parent:
            if node == parent.left:
                parent.left = right_son
            else:
                parent.right = right_son
        else:
            self.root = right_son

        right_son.left = node
        node.parent = right_son

        node.right = left_grandson
        if left_grandson:
            left_grandson.parent = node

        node.depth = self.calc_depth(node)
        node.balance = self.calc_balance(node)
        right_son.depth = self.calc_depth(right_son)
        right_son.balance = self.calc_balance(right_son)

    def middleOrder(self, node):
        if not node:
            return

        self.middleOrder(node.left)
        print(node.data)
        self.middleOrder(node.right)

    @staticmethod
    def calc_balance(node):
        left_depth = node.left.depth if node.left else 0
        right_depth = node.right.depth if node.right else 0

        return left_depth - right_depth

    def calc_depth(self, node):
        left_depth = node.left.depth if node.left else 0
        right_depth = node.right.depth if node.right else 0

        return max([left_depth, right_depth]) + 1


if __name__ == '__main__':
    a = [1, 3, 2, 4, 6, 12, 8, 15, 10, 5, 9, 7, 13, 11, 14]
    bst = AVL_Tree()
    bst.constructor(a)
    bst.insert(bst.root, 6.5)
    bst.remove(bst.root, 7)
    bst.middleOrder(bst.root)
    # bst.preOrder(bst.root)
    print('--------------------------')
    # bst.middleOrder(bst.root)
    print('--------------------------')
