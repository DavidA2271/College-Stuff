

def get_second_smallest_element(bst):
    node = bst.head
    while node.left.left is not None:
        node = node.left
    if node.right is not None:
        return node.right
    else:
        return node