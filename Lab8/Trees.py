from msilib.schema import Error


class Tree:

    class Position:
        
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):

            return not (self == other)
        
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

class BinaryTree(Tree):

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
        
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
        
    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

class ArrayBinaryTree(BinaryTree):

    def __init__(self):
        self._data = []
        self._size = 0
          
    def _validate(self, p):
        self.fill_tree(p)
        if self._data[p] is None:
            raise ValueError('p is not index of set element')
        return p

    def fill_tree(self, index):
        while index >= len(self._data):
            self._data += [None]

    def __len__(self):
        return len(self._data)
    
    def root(self):
        return self._data[1]
    
    def parent(self, p):
        self._validate(p)
        return self._data[p]

    def left(self, p):
        self._validate(p)
        self._validate(p*2)
        return self._data[p*2]

    def right(self, p):
        self._validate(p)
        self._validate(p*2+1)
        return self._data[p*2+1]
    
    def num_children(self, p):
        self._validate(p)
        self.fill_tree(2*p+1)
        count = 0
        if self._data[2*p] is not None:
            count += 1
        if self._data[2*p+1] is not None:
            count += 1
        return count

    def add_root(self, e):
        self.fill_tree(1)
        if self._data[1] is not None: raise ValueError('Root exists')
        self._size = 1
        self._data[1] = e
        return 1
    
    def add_left(self, p, e):
        self._validate(p)
        p = 2*p
        self.fill_tree(p)
        if self._data[p] is not None: raise ValueError('Left child exists')
        self._size += 1
        self._data[p] = e
        return p

    def add_right(self, p, e):
        self._validate(p)
        p = 2*p + 1
        self.fill_tree(p)
        if self._data[p] is not None: raise ValueError('Right child exists')
        self._size += 1
        self._data[p] = e
        return p
    
    def _replace(self, p, e):
        self._validate(p)
        old = self._data[p]
        self._data[p] = e
        return old

    def __str__(self):
        return str(self._data)