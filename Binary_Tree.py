class Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:

    def __init__(self):
        self._root = None

    def create_tree(self, element, left, right):
        self._root = Node(element, left._root, right._root)

    def in_order(self, root):
        if root is not None:
            self.in_order(root._left)
            print(root._element, end=' ')
            self.in_order(root._right)

    def pre_order(self, root):
        if root is not None:
            print(root._element, end=' ')
            self.pre_order(root._left)
            self.pre_order(root._right)

    def post_order(self, root):
        if root is not None:
            self.post_order(root._left)
            self.post_order(root._right)
            print(root._element, end=' ')

    def count_number_of_nodes(self, root):
        if root is not None:
            x = self.count_number_of_nodes(root._left)
            y = self.count_number_of_nodes(root._right)
            return x + y + 1
        return 0

    def height_of_tree(self, root):
        if root is not None:
            n = self.height_of_tree(root._left)
            m = self.height_of_tree(root._right)
            if n > m:
                return n + 1
            else:
                return m + 1
        return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
g = BinaryTree()
k = BinaryTree()

a = BinaryTree()

x.create_tree(12, a, a)
y.create_tree(29, a, a)
z.create_tree(72, a, a)
r.create_tree(92, a, a)
t.create_tree(30, y, a)
g.create_tree(28, x, t)
k.create_tree(86, z, r)
s.create_tree(34, g, k)
print('In order traversal:')
s.in_order(s._root)
print('\n')
print('Pre order traversal:')
s.pre_order(s._root)
print('\n')
print('Post order traversal:')
s.post_order(s._root)
print('\n')

print('Number of nodes in the tree:', s.count_number_of_nodes(s._root))
print('Height of the tree:', s.height_of_tree(s._root) - 1)