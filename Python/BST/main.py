import random
import time
from binary_search_tree import BST
from red_black_tree import RBT


def main():
    array1 = create_array(10**3)
    array2 = create_array(10**4)
    array3 = create_array(10**5)
    array4 = create_array(10**6)

    # traversal methods
    bst0 = BST()
    for i in array1:
        bst0.insert(i)
    bst0.inorder(bst0.root)
    print()
    bst0.preorder(bst0.root)
    print()
    bst0.postorder(bst0.root)
    print()

    bst1 = BST()
    bst2 = BST()
    bst3 = BST()
    bst4 = BST()
    rbt1 = RBT()
    rbt2 = RBT()
    rbt3 = RBT()
    rbt4 = RBT()

    print()
    #print("Inserting an array of size", len(array1), "into a BST took", time_method(insert_array, bst1, array1), "seconds.")
    #print("Finding an element froma BST with", len(array1), "elements took", time_method(search_tree, bst1, array1[-1]), "seconds.")
    #print("Deleting an element froma BST with", len(array1), "elements took", time_method(delete_tree, bst1, array1[int(len(array1)/2)]), "seconds.")
    #print("Inserting an array of size", len(array1), "into a RBT took", time_method(insert_array, rbt1, array1), "seconds.")
    #print("Finding an element froma RBT with", len(array1), "elements took", time_method(search_tree, rbt1, array1[-1]), "seconds.")
    #print("Deleting an element froma RBT with", len(array1), "elements took", time_method(delete_tree, rbt1, array1[int(len(array1)/2)]), "seconds.")
    print()
    print()
    #print("Inserting an array of size", len(array2), "into a BST took", time_method(insert_array, bst2, array2), "seconds.")
    #print("Finding an element froma BST with", len(array2), "elements took", time_method(search_tree, bst2, array2[-1]), "seconds.")
    #print("Deleting an element froma BST with", len(array2), "elements took", time_method(delete_tree, bst2, array2[int(len(array2)/2)]), "seconds.")
    #print("Inserting an array of size", len(array2), "into a RBT took", time_method(insert_array, rbt2, array2), "seconds.")
    #print("Finding an element froma RBT with", len(array2), "elements took", time_method(search_tree, rbt2, array2[-1]), "seconds.")
    #print("Deleting an element froma RBT with", len(array1), "elements took", time_method(delete_tree, rbt1, array1[int(len(array1)/2)]), "seconds.")
    print()
    print()
    #print("Inserting an array of size", len(array3), "into a BST took", time_method(insert_array, bst3, array3), "seconds.")
    #print("Finding an element froma BST with", len(array3), "elements took", time_method(search_tree, bst3, array3[-1]), "seconds.")
    #print("Deleting an element froma BST with", len(array3), "elements took", time_method(delete_tree, bst3, array3[int(len(array3)/2)]), "seconds.")
    #print("Inserting an array of size", len(array3), "into a RBT took", time_method(insert_array, rbt3, array3), "seconds.")
    #print("Finding an element froma RBT with", len(array3), "elements took", time_method(search_tree, rbt3, array3[-1]), "seconds.")
    #print("Deleting an element froma RBT with", len(array1), "elements took", time_method(delete_tree, rbt1, array1[int(len(array1)/2)]), "seconds.")
    print()
    print()
    #print("Inserting an array of size", len(array4), "into a BST took", time_method(insert_array, bst4, array4), "seconds.")
    #print("Finding an element froma BST with", len(array4), "elements took", time_method(search_tree, bst4, array4[-1]), "seconds.")
    #print("Deleting an element froma BST with", len(array4), "elements took", time_method(delete_tree, bst4, array4[int(len(array4)/2)]), "seconds.")
    #print("Inserting an array of size", len(array4), "into a RBT took", time_method(insert_array, rbt4, array4), "seconds.")
    #print("Finding an element froma RBT with", len(array4), "elements took", time_method(search_tree, rbt4, array4[-1]), "seconds.")
    #print("Deleting an element froma RBT with", len(array1), "elements took", time_method(delete_tree, rbt1, array1[int(len(array1)/2)]), "seconds.")
    print()

    arr5 = create_array(10**7)
    bst5 = BST()
    rbt5 = RBT()
    print("Inserting an array of size", len(arr5), "into a BST took", time_method(insert_array, bst5, arr5), "seconds.")
    print("Finding an element froma BST with", len(arr5), "elements took", time_method(search_tree, bst5, arr5[-1]), "seconds.")
    print("Deleting an element froma BST with", len(arr5), "elements took", time_method(delete_tree, bst5, arr5[int(len(arr5)/2)]), "seconds.")
    print("Inserting an array of size", len(arr5), "into a RBT took", time_method(insert_array, rbt5, arr5), "seconds.")
    print("Finding an element froma RBT with", len(arr5), "elements took", time_method(search_tree, rbt5, arr5[-1]), "seconds.")



def create_array(size):
    ''' Creates an array of the input size. 
        I made this function and used it in the sorting algorithms assignment.
    '''
    return [random.randint(0, 1000000) for _ in range(size)]


def time_method(method, tree, val):
    ''' Returns the time it takes to run a sorting method.
        I made this function and used it in the sorting algorithms assignment.
    '''
    start = time.time()
    method(tree, val)
    end = time.time()
    return end - start


def insert_array(tree, array):
    for i in array:
        tree.insert(i)


def search_tree(tree, val):
    tree.find(val)


def delete_tree(tree, val):
    tree.delete(val, tree.root)


if __name__ == '__main__':
    main()