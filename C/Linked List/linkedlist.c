
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct student
{
    int studentNumber;
    struct student *next;
};

struct student *head = NULL;
struct student *current = NULL;

// display the list
void printList()
{
    struct student *p = head;
    printf("\n["); // print a [ to denote the begining of the data

    // start from the beginning
    while (p != NULL)
    {
        printf(" %d ", p->studentNumber); // print the data in the current node, and add a space
        p = p->next; // move the pointer to the next node
    }

    printf("]"); // print the closing block bracket to denote the end of the data in the list
}

// insertion at the beginning
void insertatbegin(int data)
{
    // create a link
    //malloc = memory allocation
    struct student *lk = (struct student *)malloc(sizeof(struct student));

    lk->studentNumber = data;

    // point it to old first node
    lk->next = head;

    // point first to new first node
    head = lk;
}

void insertatend(int data)
{
    // create a link
    struct student *lk = (struct student *)malloc(sizeof(struct student));
    lk->studentNumber = data;
    struct student *linkedlist = head;

    // point it to old first node
    while (linkedlist->next != NULL)
        linkedlist = linkedlist->next;

    // point first to new first node
    linkedlist->next = lk;
}

void insertafternode(struct student *list, int data)
{
    struct student *lk = (struct student *)malloc(sizeof(struct student));
    lk->studentNumber = data;
    lk->next = list->next;
    list->next = lk;
}

void deleteatbegin()
{
    head = head->next;
}

void deleteatend()
{
    struct student *linkedlist = head;
    while (linkedlist->next->next != NULL)
        linkedlist = linkedlist->next;
    linkedlist->next = NULL;
}

void deletenode(int key)
{
    struct student *temp = head, *prev;

    if (temp != NULL && temp->studentNumber == key)
    {
        head = temp->next;
        return;
    }

    // Find the key to be deleted
    while (temp != NULL && temp->studentNumber != key)
    {
        prev = temp;
        temp = temp->next;
    }

    // If the key is not present
    if (temp == NULL)
        return;

    // Remove the node
    prev->next = temp->next;
}

int searchlist(int key)
{
    struct student *temp = head;
    while (temp != NULL)
    {
        if (temp->studentNumber == key)
        {
            return 1;
        }
        temp = temp->next;
    }

    return 0;
}

void main()
{
    int k = 0;
    insertatbegin(12);
    insertatbegin(22);
    //insertatend(30);
    //insertatend(44);
    insertatbegin(50);
    insertafternode(head->next->next, 33);
    printf("Linked List: ");

    // print list
    printList();
    /*deleteatbegin();
    deleteatend();
    deletenode(12);
    printf("\nLinked List after deletion: ");

    // print list
    printList();
    insertatbegin(4);
    insertatbegin(16);
    printf("\nUpdated Linked List: ");
    printList();

    k = searchlist(16);
    if (k == 1)
        printf("\nElement is found");

    else
        printf("\nElement is not present in the list");*/
}