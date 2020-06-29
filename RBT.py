####################################################################
# 红黑树
#
# 根节点和叶子节点是黑色的
# 红色节点的两个孩子都是黑色的
# 从任一节点到其叶子节点的所有简单路径都包含相同数量的黑色节点
# 推论： 从根节点到叶子节点的最长可能路径不多于最短可能路径长度的两倍
####################################################################

BLACK = True
RED = False


class TreeNode(object):
    def __init__(self, value):
        self.color = RED
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class RBTree(object):
    def __init__(self):
        self.root = None

    def leftRotate(self, node):
        rChild = node.right
        parent = node.parent

        node.right = rChild.left
        if rChild.left:
            rChild.left.parent = node

        rChild.parent = node.parent
        if parent is None:
            self.root = rChild
        else:
            if parent.left == node:
                parent.left = rChild
            else:
                parent.right = rChild

    def rightRotate(self, node):
        lChild = node.left
        parent = node.parent

        node.left = lChild.right
        if lChild.right:
            lChild.right.parent = node

        lChild.parent = node.parent
        if parent is None:
            self.root = lChild
        else:
            if parent.left == node:
                parent.left = lChild
            else:
                parent.right = lChild

    def insert(self, node):
        p = self.root

        if p is None:
            node.color = BLACK
            self.root = node
            return

        while p:
            if node.value < p.value:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    break
                else:
                    p = p.right

        self.adjust_insert(node)

    def adjust_insert(self, node):

        # parent exists and with red color
        while node.parent and node.parent.color == RED:
            parent = node.parent
            grand = parent.parent
            # parent is left child of grand
            if parent == grand.left:
                uncle = grand.right
                # uncle exists and uncle is red
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grand.color = RED
                    node = grand
                    continue
                # uncle not exists or uncle is black
                # current is right child of parent
                if node == parent.right:
                    self.leftRotate(parent)
                    temp = parent
                    parent = node
                    node = temp
                # current is left child of parent
                parent.color = BLACK
                grand.color = RED
                self.rightRotate(grand)
            # parent is right child of grand
            else:
                uncle = grand.left
                # uncle exists and uncle with color red
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grand.color = RED
                    node = grand
                    continue
                # uncle not exists or uncle is black
                # current is left child of parent
                if node == parent.left:
                    self.rightRotate(parent)
                    temp = parent
                    parent = node
                    node = parent
                # current is right child of parent
                parent.color = BLACK
                grand.color = RED
                self.leftRotate(grand)

        self.root.color = BLACK

    def remove(self, node):
        parent = node.parent
        if node.left and node.right:
            replace = node.right
            while replace.left:
                replace = replace.left

            if parent:
                if node == parent.left:
                    parent.left = replace
                else:
                    parent.right = replace
            else:
                self.root = replace

            rchild = replace.right
            rparent = replace.parent

            rcolor = replace.color

            if rparent == node:
                rparent = replace
            else:
                if rchild:
                    rchild.parent = rparent
                rparent.left = rchild

                replace.right = node.right
                node.right.parent = replace
            replace.parent = node.parent
            replace.color = node.color
            replace.left = node.left
            node.left.parent = replace

            if rcolor == BLACK:
                self.adjust_remove(rchild, rparent)

            node = None
            return

        # node only has left child or only has right child
        child = node.left if node.left else node.right

        color = node.color

        if child:
            child.parent = parent

        if parent:
            if node == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child

        if color == BLACK:
            self.adjust_remove(child, parent)

    def adjust_remove(self, node, parent):
        while (node is None or node.color == BLACK) and node != self.root:
            if node == parent.left:
                uncle = parent.right
                if uncle.color == RED:
                    uncle.color = BLACK
                    parent.color = RED
                    self.leftRotate(parent)
                    uncle = parent.right

                if (uncle.left is None or uncle.left.color == BLACK) and (uncle.right is None or uncle.right.color == BLACK):
                    uncle.color = RED
                    node = parent
                    parent = node.parent
                else:
                    # case 3: node is black; uncle is black;
                    if uncle.right is None or uncle.right.color == BLACK:
                        temp = uncle.color
                        uncle.color = uncle.left.color
                        uncle.left.color = temp
                        self.rightRotate(uncle)
                        uncle = parent.right

                    # case 4: node is black; uncle is black; uncle's two children both are red
                    temp = parent.color
                    parent.color = uncle.color
                    uncle.color = temp
                    uncle.right.color = BLACK
                    self.leftRotate(parent)
                    node = self.root
                    break
            else:
                uncle = parent.right
                if uncle.color == RED:
                    uncle.color = BLACK
                    parent.color = RED
                    self.rightRotate(parent)
                    uncle = parent.left

                if (uncle.left is None or uncle.left.color == BLACK) and (uncle.right is None or uncle.right.color == BLACK):
                    uncle.color = RED
                    node = parent
                    parent = node.parent
                else:
                    if uncle.left is None or uncle.left.color == BLACK:
                        uncle.right.color = BLACK
                        uncle.color = RED
                        self.leftRotate(uncle)
                        uncle = parent.left

                    uncle.color = parent.color
                    parent.color = BLACK
                    uncle.left.color = BLACK
                    self.rightRotate(parent)
                    node = self.root
                    break

        if node:
            node.color = BLACK
