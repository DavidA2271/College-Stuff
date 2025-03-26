import binary_search_tree
from node import Node


class RBT(binary_search_tree.BST):
    def insert(self, value):
        n = super().insert(value)
        self.insert_after(n)
    def insert_after(self, insertedNode):
        ''' After inserting a new node. Its color and position must be readjusted. '''
        while insertedNode.parent is not None and insertedNode.parent.color == 'red':
            if insertedNode.parent == insertedNode.grandparent().left:
                uncleNode = insertedNode.uncle()
                if uncleNode is not None and uncleNode.color == 'red':
                    insertedNode.parent.color = 'black'
                    uncleNode.color = 'black'
                    insertedNode.grandparent().color = 'red'
                    insertedNode = insertedNode.grandparent()
                else:
                    if insertedNode == insertedNode.parent.right:
                        insertedNode = insertedNode.parent
                        self.rotate_left(insertedNode)
                    insertedNode.parent.color = 'black'
                    insertedNode.grandparent().color = 'red'
                    self.rotate_right(insertedNode.grandparent())
            else:
                uncleNode = insertedNode.uncle()
                if uncleNode is not None and uncleNode.color == 'red':
                    insertedNode.parent.color = 'black'
                    uncleNode.color = 'black'
                    insertedNode.grandparent().color = 'red'
                    insertedNode = insertedNode.grandparent()
                else:
                    if insertedNode == insertedNode.parent.left:
                        insertedNode = insertedNode.parent
                        self.rotate_right(insertedNode)
                    insertedNode.parent.color = 'black'
                    insertedNode.grandparent().color = 'red'
                    self.rotate_left(insertedNode.grandparent())
        self.root.color = 'black'
    def find(self, value, curr_node=None):
        ''' Same as regular BST '''
        return super().find(value, curr_node)
    def delete(self, value, curr_node):
        ''' Same as BST delete, but needs readjusting afterwords. '''
        n = self.find(value, curr_node)
        super().delete(value, curr_node)
        self.delete_after(n)
    def delete_after(self, node):
        ''' Fixes color/position after deleting an element. '''
        while node != self.root and node.color == 'black':
            if node == node.parent.left:
                sibling = node.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.rotate_left(node.parent)
                    sibling = node.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = node.sibling()
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    if sibling.right:
                        sibling.right.color = 'black'
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self.rotate_right(node.parent)
                    sibling = node.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = node.sibling()
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    if sibling.left:
                        sibling.left.color = 'black'
                    self.rotate_right(node.parent)
                    node = self.root
        node.color = 'black'
    def rotate_left(self, node):
        ''' Rotates section surrounding node to the left '''
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child
    def rotate_right(self, node):
        ''' Rotates section surrounding node to the right '''
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child
