#!python
from linkedlist import LinkedList
class Stack(list):
    # push to end
    # pop from end
    # peek end
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
        return len(self) == 0

    def length(self):
        """Return the number of items in this stack"""
        return len(self)

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self[-1]

    def push(self, item):
        """Push the given item onto this stack"""
        self.append(item)

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty:
            raise ValueError
        else:
            return super(Stack, self).pop()

# class Stack(object):
#
#     # push - append to head
#     # pop - remove from head
#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         self.data = LinkedList()
#         if iterable:
#             for item in iterable:
#                 self.push(item)
#
#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.length())
#
#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         return super(Stack, self).is_empty()
#
#     def length(self):
#         """Return the number of items in this stack"""
#         return self.size
#
#     def peek(self):
#         """Return the top item on this stack without removing it,
#         or None if this stack is empty"""
#         if self.is_empty():
#             return None
#         else:
#             return self.data.head.data
#
#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.prepend(item)
#
#     def pop(self):
#         """Return the top item and remove it from this stack,
#         or raise ValueError if this stack is empty"""
#         if self.is_empty():
#             raise ValueError
#         else:
#             first_item = self.first()
#             self.delete(first_item)
#             return first_item
