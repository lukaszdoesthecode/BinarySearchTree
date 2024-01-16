from Binary_search_tree import Node, insert, tree2digraph, node_sort, node_rsort
from IPython import display

root = Node(8, 'eight')
insert(root, 5, 'five')
insert(root, 2, 'two')
result = node_sort(root)
print(result)
