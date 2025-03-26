
#include <stdio.h>

int main(void)
{
    const int totalNumbers = 5;
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int num4 = 0;
    int num5 = 0;

    printf("Enter %d numbers.\n", totalNumbers);
    scanf("%d%d%d%d%d", &num1, &num2, &num3, &num4, &num5);

    int sum = num1 + num2 + num3 + num4 + num5;
    double average = (double)sum / totalNumbers;

    printf("\n\n");
    printf("The sum of your numbers is: %d\n", sum);
    printf("The average is: %f", average);    

    return 0;
}
