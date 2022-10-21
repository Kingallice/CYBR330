from Trees import ArrayBinaryTree
from Trees import LinkedBinaryTree

y = LinkedBinaryTree()

y._add_root('A')
y._add_left(y.root(),'B')
y._add_right(y.root(), 'C')

print(y.num_children(y.root()))

x = ArrayBinaryTree()

root = x.add_root('A')
left = x.add_left(root, 'B')
right = x.add_right(root, 'D')
x.add_left(left, 'E')

print(str(x))