import uuid


class Node:
    def __init__(self, key, val):
        self.id = uuid.uuid1()
        self.key, self.val = key, val
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node( ' + str(self.key) + ', ' + str(self.val) + ' )'

    def __eq__(self, other):
        return self.id == other.id


class LinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.prev = self._sentinel
        self._sentinel.next = self._sentinel
        self._curr = self._sentinel
        self._size = 0

    @property
    def curr(self):
        return self._curr

    @property
    def size(self):
        return self._size

    def append(self, node):
        nextNode = self._sentinel.prev
        nextNode.next = node
        node.prev = nextNode
        node.next = self._sentinel
        self._sentinel.prev = node
        self._size += 1
    
    def pop(self, node=None):
        if not node:
            node = self._sentinel.next

        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        if node == self._curr:
            self._curr = node.next

        self._size -= 1
        return node

    def validate(self):
        node = self._sentinel.next
        while True:
            if node != node.next.prev: return False
            if node != node.prev.next: return False
            if node == self._sentinel: break
            node = node.next
        return True

    def __repr__(self):
        string = ['None']
        node = self._sentinel.next
        while node and node != self._sentinel:
            s = str(node)
            if node == self._curr:
                s += "[current]"
            string.append(s)
            node = node.next

        string += ['None']
        return "<->".join(string)

    def __iter__(self):
        return self
    
    def __next__(self):
        self._curr = self._curr.next
        if self._curr == self._sentinel:
            raise StopIteration
        return self._curr
        

class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._nodes = {}
        self._linkedList = LinkedList()

    def put(self, key, val):
        if self._linkedList.size >= self._capacity\
                and key not in self._nodes:
            self._evict()

        if key in self._nodes:
            self._update(key, val)
            return

        self._nodes[key] = Node(key, val)
        self._linkedList.append(self._nodes[key])

    def get(self, key):
        if key not in self._nodes: return -1
        node = self._nodes[key]
        # Re-insert used key into the list
        self._linkedList.append(self._linkedList.pop(node))
        return node.val

    def _update(self, key, val):
        node = self._nodes[key]
        node.val = val
        self._linkedList.append(self._linkedList.pop(node))

    def _evict(self):
        node = self._linkedList.pop()
        self._nodes.pop(node.key)
