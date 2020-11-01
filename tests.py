import unittest
from lrucache.lrucache import *

class LinkedListTest(unittest.TestCase):
    def test_empty(self):
        li = LinkedList()
        self.assertTrue(li.validate())
        self.assertEqual(str(li), "None<->None")
        self.assertEqual(li._sentinel.prev, li._sentinel)
        self.assertEqual(li._sentinel.next, li._sentinel)

    def test_add_and_remove(self):
        li = LinkedList()
        node = Node(1,1)
        li.append(node)
        li.pop(node)
        self.assertTrue(li.validate())
        self.assertEqual(li._sentinel.prev, li._sentinel)
        self.assertEqual(li._sentinel.next, li._sentinel)

    def test_add_multiple(self):
        li = LinkedList()
        node1, node2, node3 = Node(1,1), Node(2,2), Node(3,3)
        li.append(node1)
        li.append(node2)
        li.append(node3)
        self.assertTrue(li.validate())
        self.assertEqual(li._sentinel.prev, node3)
        self.assertEqual(li._sentinel.next, node1)

    def test_remove_curr(self):
        li = LinkedList()
        node1, node2, node3 = Node(1,1), Node(2,2), Node(3,3)
        li.append(node1)
        li.append(node2)
        li.append(node3)
        self.assertTrue(li.validate())
        node = next(li)
        self.assertEqual(node, node1)
        self.assertTrue(li.validate())
        li.pop(node1)
        self.assertTrue(li.validate())
        self.assertEqual(li.curr, node2)
        node4 = Node(4,4)
        li.append(node4)
        li.pop(node4)
        li.pop(node2)
        self.assertTrue(li.validate())
        self.assertEqual(li.curr, node3)


class LRUCacheTest(unittest.TestCase):
    def test_get_invalid(self):
        cache = LRUCache(4)
        cache.put(1,1)
        cache.put(2,2)
        self.assertEqual(-1, cache.get(3))

    def test_evict_case1(self):
        cache = LRUCache(3)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(2)
        self.assertEqual(1, cache.get(1))
        cache.put(3,3)
        cache.put(4,4)
        self.assertEqual(-1, cache.get(2))

    def test_evict_case2(self):
        cache = LRUCache(4)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(2)
        self.assertEqual(1, cache.get(1))
        cache.put(3,3)
        cache.put(4,4)
        cache.get(2)
        cache.put(5,5)
        self.assertEqual(-1, cache.get(1))

    def test_put_same_key1(self):
        cache = LRUCache(4)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(2)
        self.assertEqual(1, cache.get(1))
        cache.put(3,3)
        cache.put(4,4)
        cache.put(4,7)
        self.assertEqual(7, cache.get(4))

    def test_put_same_key1(self):
        cache = LRUCache(4)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(2)
        self.assertEqual(1, cache.get(1))
        cache.put(3,3)
        cache.put(4,4)
        cache.put(4,7)
        cache.put(3,5)
        self.assertEqual(5, cache.get(3))

    def test_put_evicted_key1(self):
        cache = LRUCache(4)
        cache.put(1,1)
        cache.put(2,2)
        cache.get(2)
        self.assertEqual(1, cache.get(1))
        cache.put(3,3)
        cache.put(4,4)
        cache.put(4,7)
        cache.put(1,8)
        self.assertEqual(8, cache.get(1))


if __name__ == '__main__':
    unittest.main()
