from typing import MutableMapping
from PositionalList import PositionalList

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""

    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

class UnsortedTableMap(MapBase):
    """Map implementation using an unorder list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwirting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find match key
        self._table.append(self._Item(k, v))
    
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        """Returns number of items in the map."""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key

# A
class PositionalListUnsortedTableMap(MapBase):
    """UnsortedTableMap implementation using PositionalList class"""

    def __init__(self):
        """Create an empty map using Positional List"""
        self._table = PositionalList()

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwirting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find match key
        self._table.add_last(self._Item(k, v))
    
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if self._table.find(self._Item(k, self[k]))[1]:
            self._table.delete(self._table.find(self._Item(k, self[k]))[0])
            return
        raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        """Returns number of items in the map."""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key

    # B
    def pop(self, k):
        """Removes and returns value at key k"""
        val = self[k]
        del self[k]
        return val