import graphviz


class Node:
    """Object representing the node of the binary search tree."""

    def __init__(self, key, value):
        """
        Initialization of the node of binary search tree.
        :param key: (int or float) the key of the binary search tree, should be unique.
        :param value: (any) value of the binary search tree.
        :return: None
        """
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __getitem__(self, key):
        """
        Returns the key and a value of the chosen node by a key in form of a tuple. In case the node with exact key does
        not exist - the function returns key error.
        :param key: (int or float) the key of the node of the binary search tree which is about to be searched.
        :return key_chosen_node: (int or float) the key of the searched node of the binary search tree.
        :return value_chosen_node: (any) the value of the searched node of the binary search tree.
        """
        nodes_sorted = node_sort(self)

        for key_chosen_node, value_chosen_node in nodes_sorted:
            if key_chosen_node == key:
                return key_chosen_node, value_chosen_node

        raise KeyError(f"Key {key} not found in the binary search tree.")

    def __setitem__(self, key, value):
        """
        Sets the value of the chosen node to a desired value of any data type. In case the node with exact key does
        not exist - the function returns key error.
        :param key: (int or float) the key of the node of the BST whose value is to be changed.
        :param value: (any) the new value of the changed node of the BST.
        :return: None
        """
        nodes_sorted = node_sort(self)
        for key_chosen_node, value_chosen_node in nodes_sorted:
            if key_chosen_node == key:
                insert(self, key, value)
                return None

        raise KeyError(f"Key {key} not found in the binary search tree.")

    def __delitem__(self, key):
        """
       Deletes the node in the BST of the given key. In case the node with exact key does not exist - the function
       returns key error.
       :param key: (int or float) the key of the node of the BST which is about to be deleted.
       :return: None
       """
        nodes_sorted = node_sort(self)
        for key_chosen_node, value_chosen_node in nodes_sorted:
            if key_chosen_node == key:
                remove(self, key)
                return None

        raise KeyError(f"Key {key} not found in the binary search tree.")


def insert(node, key, value):
    """
    Inserts new node into the binary search tree. In case the node with the key which was previously used is inserting
    into the tree - the value of previously created node will be updated to the value of the new one.
    :param node: (node) root of node of the binary search tree.
    :param key: (int or float) the key of the binary search tree, should be unique.
    :param value: (any) value of the binary search tree.
    :return: None
    """
    if key < node.key:
        if node.left is None:
            node.left = Node(key, value)
        else:
            insert(node.left, key, value)
    elif key > node.key:
        if node.right is None:
            node.right = Node(key, value)
        else:
            insert(node.right, key, value)
    else:
        node.value = value


def node_sort(node):
    """
    Sorts all the elements of binary search tree by its key, going from the lowest, to the highest.
    :param node: (node) root of node of the binary search tree.
    :return nodes_sorted: (list of tuples) List of all the elements of binary search tree by its key, going from the
    lowest, to the highest. Consisting of tuples consisting of key and value of each node.
    """
    nodes_sorted = []
    if node is not None:
        nodes_sorted += node_sort(node.left)
        nodes_sorted.append((node.key, node.value))
        nodes_sorted += node_sort(node.right)
    return nodes_sorted


def remove(node, key):
    """
    Deletes the node with the given key from the tree. In case the removed node has children, the children are linked
    with the "grandparent" of the children, with fulfilling the ruled of binary search tree. To be exact:
    If node to be deleted has one child - the child goes to the place of the deleted node.
    If node to be deleted has two child - the child with the next higher key value (successor) that is the leftmost node
    in the right offspring of the deleted one goes into plate of removed node. In place of the transferred successor,
    its right descendant (if any) should be inserted.
    :param node: (node) root node of the binary search tree.
    :param key: (int or float) the key of the binary search tree, should be unique.
    :return node: (node) binary search tree with removed node of matching key.
    """
    assert node is not None, "The specified key does not exist."

    if key == node.key:
        if node.right is None:  # Also includes the situation
            return node.left  # when node is a leaf.
        elif node.left is None:
            return node.right
        else:
            # Searching for the right successor and its parent:
            successor_parent = node
            successor = node.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Attach the right descendant of the successor to its parent :
            if successor_parent is not node:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

            # Attach the descendants of the deleted node to successor:
            successor.left = node.left
            successor.right = node.right

            # The successor reference will be returned
            # to the parent of the deleted node:
            return successor

    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)

    return node


def node_rsort(node):
    """
    Sorts all the elements of binary search tree by its key in reversed order, going from the highest, to the lowest.
    :param node: (node) root node of the binary search tree.
    :return reversed_sorted_nodes: (list of tuples) List of all the elements of binary search tree by its key, going
    from the highest, to the lowest. Consisting of tuples consisting of key and value of each node.
    """
    nodes_r_sorted = []

    if node.right is not None:
        nodes_r_sorted += node_rsort(node.right)
    nodes_r_sorted.append((node.key, node.value))
    if node.left is not None:
        nodes_r_sorted += node_rsort(node.left)
    return nodes_r_sorted


def tree2digraph(node, g=None):
    """
    Returns graphical representation of the binary search tree.
    :param node: (node) root node of the binary search tree.
    :param g: (str) string representing which type of visualization should be created.
    :return g: (graphviz.graphs.Digraph) object of digraph of the graphviz library.
    """
    if g is None:
        g = graphviz.Digraph()
        g.engine = 'dot'

    if node is not None:

        g.node(str(node.key))

        if node.left is not None:
            g.edge(str(node.key), str(node.left.key), 'L')
        if node.right is not None:
            g.edge(str(node.key), str(node.right.key), 'R')

        tree2digraph(node.left, g)
        tree2digraph(node.right, g)

    return g
