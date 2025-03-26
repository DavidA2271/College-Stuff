
#include <stdio.h>

int main(void) {
    char name[100];
    int age;

    printf("Input your name and age.");
    scanf("%s%d", &name, &age);
    printf("Hello %s, next year you will be %d.", name, age + 1);
    return 0;
}
