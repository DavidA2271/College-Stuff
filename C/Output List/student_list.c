
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct student
{
    int studentNumber;
    char name[20];
    char major[8];
    struct student *next;
};

struct student *head = NULL;
struct student *current = NULL;

void printList()
{
    struct student *p = head;
    printf("\n[\n");

    while (p != NULL)
    {
        printf("Student Number: %d, Name: %s, Major: %s \n", p->studentNumber, p->name, p->major);
        p = p->next;
    }

    printf("]");
}

struct student *newStudent(int number, char name[], char major[])
{
    struct student *lk = /*(struct student *)*/malloc(sizeof(struct student));

    lk->studentNumber = number;
    int strlength = strlen(name);
    int i;
    for (i = 0; i < strlength; i++)
    {
        lk->name[i] = name[i];
    }
    lk->name[i] = '\0';

    strlength = strlen(major);
    for (i = 0; i < strlength; i++)
    {
        lk->major[i] = major[i];
    }
    lk->major[i] = '\0';

    lk->next = NULL;

    return lk;
} 

void insertatbegin(struct student *lk)
{
    lk->next = head;
    head = lk;
}

void searchlist(char major[])
{
    
    struct student *temp = head;
    while (temp != NULL)
    {
        if (strcmp(temp->major, major) == 0)
        {
            printf("Student Number: %d, Name: %s, Major: %s \n", temp->studentNumber, temp->name, temp->major);
        }
        temp = temp->next;
    }
}

void main()
{
    struct student *cis2 = newStudent(92, "Mark", "CIS");
    struct student *cis1 = newStudent(37, "Rachel", "CIS");
    struct student *cit1 = newStudent(15, "Harold", "CIT");

    insertatbegin(cis1);
    insertatbegin(cis2);
    insertatbegin(cit1);
    printf("Linked List: ");
    printList();

    char major[10];
    printf("\n\n");
    printf("Enter a major: ");
    scanf("%s", major);
    searchlist(major);
    printf("\n\n");

    struct student *cit2 = newStudent(113, "Shannon", "CIT");
    insertatbegin(cit2);
    printf("Linked List: ");
    printList();

    printf("\n\n");
    printf("Enter a major: ");
    scanf("%s", major);
    searchlist(major);
    printf("\n\n");
}