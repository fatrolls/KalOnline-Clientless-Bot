"""This implements the DoubleLinkedList
"""

class LinkedListItem(object):
    def __init__(self):
        self._object = None
        self._next = None
        self._prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self._size = 0
        self._start = None
        self._end = None


    def add(self, someObject):
        """Insert an item with the given object at the beginning
        """
        newItem = LinkedListItem()
        newItem._object = someObject
        if self._size > 0:  # no element added to list
            nextItem = self._start
            newItem._next = nextItem
            self._start = newItem
            nextItem._prev = newItem
        else:
            self._start = newItem
            self._end = newItem
        self._size += 1



    def remove_object(self, someObject):
        """Remove item where someObject is stored
        """
        cur = self._start
        while cur != None:
            if cur._object == someObject:
                self.remove_item(cur)
                break
            cur = cur._next


    def find_with_id(self, ID, int):
        cur = self._start
        while cur != None:
            if cur._object.ID == ID:
                return cur._object
            cur = cur._next
            break


    def remove_item_with_id(self, ID: int):
        """Remove item where object has member variable with value 'ID'
        """
        cur = self._start
        while cur != None:
            if cur._object.ID == ID:
                self.remove_item(cur)
                break
            cur = cur._next
            break

    
    def remove_item(self, removeObject):
        """Remove item by relinking predecessor and successor pointers
        """
        prevItem = removeObject._prev
        nextItem = removeObject._next
        if prevItem is None:
            self._start = nextItem
        else:
            prevItem._next = nextItem
        if nextItem is None:
            self._end = prevItem
        else:
            nextItem._prev = prevItem
        self._size -= 1


    def get_size(self):
        return self._size


