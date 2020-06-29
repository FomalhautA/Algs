from collections import defaultdict


class TreeNode(object):

    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.final = False


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.query_str = ''
        self.tree = TreeNode()
        for word in words:
            current_node = self.tree
            for letter in word[::-1]:
                current_node = current_node.children[letter]
            current_node.final = True

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.query_str += letter
        if len(self.query_str) > 2000:
            self.query_str = self.query_str[1:]

        current_node = self.tree
        l = len(self.query_str)
        idx = 1
        while idx <= l:
            letter = self.query_str[-idx]

            if letter not in current_node.children:
                return False

            current_node = current_node.children[letter]

            if current_node.final:
                return True

            idx += 1

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
