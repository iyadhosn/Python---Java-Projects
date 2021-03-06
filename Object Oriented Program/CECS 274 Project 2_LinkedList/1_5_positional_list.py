class _DoublyLinkedBase:
    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        buffer = []
        current_node = self._header
        while current_node != self._trailer:
            buffer.append(current_node._element)
            current_node = current_node._next
        return buffer.__str__()


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

        def __str__(self):
            return str(self._node._element)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def __str__(self):
        s = ""
        for element in self:
            s += str(element) +","
        return s

def parisum(L: PositionalList, V: int):
    # sets front and back equal to the first and last element in the linked list
    front = L.first()
    back = L.last()
    # This condition will always be true because the list is sorted
    while front.element() < back.element():
        # If the sum of the front and back element is greater than V
        # shift the back element left by one because the numbers are to big.
        if front.element() + back.element() > V:
            back = L.before(back)
        # If the sum of the front and back element is less than V
        # shift the front element right by one because the numbers are to small
        elif front.element() + back.element() < V:
            front = L.after(front)
        # If the two nodes are equal to V we have found a pair
        elif front.element() + back.element() == V:
             print((front.element(), back.element()), end=' ')
             back = L.before(back)
        # If there is no pair return None
        else:
            print(None)
    print()


p_list = PositionalList()
p2 = p_list.add_last(2)
p_list.add_last(4)
p_list.add_last(7)
p_list.add_last(9)
p_list.add_last(11)
p_list.add_last(13)
p_list.add_last(17)
p_list.add_last(22)
print(p_list)   # prints 2,4,7,9,11,13,17,22
# I took the print statement off parisum and put it in the function
# cuz it worked better like that with my code.
parisum(p_list, 15)  # prints (2,13) or (4,11)
print(parisum(p_list, 36))  # prints None
