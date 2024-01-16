import unittest
from Binary_search_tree import Node, insert, remove, node_sort, node_rsort


# __init__ method test
class TestInitFunctionBST(unittest.TestCase):
    # Case 1 - value is a string
    def test_first_case_init(self):
        key = 20
        value = 'twenty'
        node = Node(key, value)
        self.assertEqual(node.key, key)
        self.assertEqual(node.value, value)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    # Case 2 - value is a number
    def test_second_case_init(self):
        key = 6
        value = 6
        node = Node(key, value)
        self.assertEqual(node.key, key)
        self.assertEqual(node.value, value)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    # Case 3 - value is a tuple
    def test_third_case_init(self):
        key = 9
        value = (3, 'three')
        node = Node(key, value)
        self.assertEqual(node.key, key)
        self.assertEqual(node.value, value)
        self.assertIsNone(node.left)

    # Case 4 - value is a tuple, key is float
    def test_fourth_case_init(self):
        key = 9.01
        value = (3, 'three')
        node = Node(key, value)
        self.assertEqual(node.key, key)
        self.assertEqual(node.value, value)
        self.assertIsNone(node.left)


# __getitem__ test function
class TestGetItemFunctionBST(unittest.TestCase):
    # Case 1 - finding existing node
    def test_first_case_getitem(self):
        root = Node(10, 'ten')
        result = root[10]
        self.assertEqual(result, (10, 'ten'))

    # Case 2 - attempting to find the non-existing node
    def test_second_case_getitem(self):
        root = Node(5, "five")
        with self.assertRaises(KeyError):
            result = root[3]


# __setitem__ test function
class TestSetItemFunctionBST(unittest.TestCase):
    # Case 1 - setting the existing node value to the new value
    def test_first_case_setitem(self):
        root = Node(4, "four")
        root.__setitem__(4, "four_test")
        result = root[4]
        self.assertEqual(result, (4, "four_test"))

    # Case 2 - attempting to set the non-existing node value to the new one
    def test_second_case_setitem(self):
        root = Node(4, "four")
        with self.assertRaises(KeyError):
            root.__setitem__(5, "five_test")


# __delitem__ test function
class TestDelItemTestFunction(unittest.TestCase):
    # Case 1 - deleting the existing node
    def test_first_case_delitem(self):
        root = Node(4, "four")
        result = root.__delitem__(4)
        self.assertEqual(result, None)

    # Case 2 - attempting to delete the non-existing node
    def test_second_case_delitem(self):
        root = Node(4, "four")
        with self.assertRaises(KeyError):
            root.__delitem__(5)


# insert function test
class TestInsertTestFunction(unittest.TestCase):
    # Case 1 - inserting to the left side
    def test_first_case_insert(self):
        root = Node(10, 'ten')
        insert(root, 5, 'five')

        self.assertEqual(root.left.key, 5)
        self.assertEqual(root.left.value, 'five')
        self.assertIsNone(root.right)

    # Case 2 - inserting to the right side
    def test_second_case_insert(self):
        root = Node(10, 'ten')
        insert(root, 20, 'twenty')

        self.assertEqual(root.right.key, 20)
        self.assertEqual(root.right.value, 'twenty')
        self.assertIsNone(root.left)


# remove function test
class TestRemoveTestFunction(unittest.TestCase):
    # Case 1 - removing "child-less" children
    def test_first_case_remove(self):
        root = Node(10, 'ten')
        insert(root, 5, 'five')
        remove(root, 5)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    # Case 2 - removing children having children
    def test_second_case_remove(self):
        root = Node(10, 'ten')
        insert(root, 5, 'five')
        insert(root, 2, 'two')
        remove(root, 5)
        self.assertIsNone(root.right)
        self.assertEqual(root.left.key, 2)
        self.assertEqual(root.left.value, 'two')


# node sort function
class TestNodeSortTestFunction(unittest.TestCase):
    # Case 1 - one element BST
    def test_first_case_node_sort(self):
        root = Node(10, 'ten')
        result = node_sort(root)
        self.assertEqual(result, [(10, 'ten')])

    # Case 2 - multi-element BST
    def test_second_case_node_sort(self):
        root = Node(10, 'ten')
        insert(root, 5, 'five')
        insert(root, 2, 'two')
        result = node_sort(root)
        self.assertEqual(result, [(2, 'two'), (5, 'five'), (10, 'ten')])


# node rsort function
class TestNodeRsortTestFunction(unittest.TestCase):
    def test_first_case_node_rsort(self):
        root = Node(10, 'ten')
        result = node_rsort(root)
        self.assertEqual(result, [(10, 'ten')])

    # Case 2 - multi-element BST
    def test_second_case_node_rsort(self):
        root = Node(8, 'eight')
        insert(root, 5, 'five')
        insert(root, 2, 'two')
        result = node_rsort(root)
        self.assertEqual(result, [(8, 'eight'), (5, 'five'), (2, 'two')])


if __name__ == '__main__':
    unittest.main()
