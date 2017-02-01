#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        super(Stack, self).__init__()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        super(Stack, self).is_empty()

    def length(self):
        """Return the number of items in this stack"""
        return self.size

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self.first()

    def push(self, item):
        """Push the given item onto this stack"""
        # TODO: push given item
        pass

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        # TODO: pop top item, if any
        pass
