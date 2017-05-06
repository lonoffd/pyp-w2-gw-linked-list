from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        self._count = 0
        if elements:
            for element in elements:
                self.append(element)

    def __str__(self):
        inner_string = ", ".join(str(element) for element in self)
        return "[{}]".format(inner_string)

    def __len__(self):
        return self._count

    def __iter__(self):
        current_node = self.start
        while current_node is not None:
            yield current_node.elem
            current_node = current_node.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= self._count:
            raise IndexError
        it = iter(self)
        for i in range(index):
            next(it)
        return next(it)

    def __add__(self, other):
        new_ll = LinkedList()
        for elem in self:
            new_ll.append(elem)
        for elem in other:
            new_ll.append(elem)
        return new_ll

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all(n1 == n2 for n1, n2 in zip(self, other))

    def __ne__(self, other):
        return not self == other

    def append(self, elem):
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = self.end.next

        self._count += 1

    def count(self):
        return self._count

    def pop(self, index=None):
        if index is None:
            index = self._count - 1

        if index >= self._count or self._count == 0:
            raise IndexError

        if index == 0:
            # pop start item in list, so just need to get that item
            # and then set start to be the next item
            elem = self.start.elem
            self.start = self.start.next
        else:
            previous_node = self.start
            current_node = self.start.next

            for i in range(index - 1):
                previous_node = current_node
                current_node = current_node.next

            elem = current_node.elem
            previous_node.next = current_node.next

            if index == self._count - 1:
                # deal with popping the final element
                self.end = previous_node

        self._count -= 1
        return elem
