

def reverse_list(arr):
    node = arr.head
    next = None
    prev = None
    while node is not None:
        next = node.next
        node.next = prev
        prev = node
        node = next

