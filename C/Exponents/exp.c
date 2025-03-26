
#include <stdio.h>
#include <math.h>

int main(void)
{
    int highest_power, max_number;
    int i;
    int j;

    printf("Input the maximum base integer and highest power you want.");
    scanf("%d%d", &max_number, &highest_power);
    printf(";;;;; TABLE OF POWERS ;;;;;\n");
    i = 0;
    do {
        if (i == 0)
            printf("           Base");
        else
            printf("    Power of %d  ", i + 1);
        ++i;
    } while (i < highest_power);
    printf("\n");
    for (i = 1; i <= max_number; ++i){
        for (j = 1; j <= highest_power; ++j) {
            double d = pow(i, j);
            int e = (int)d;
            printf("         |  %d  |", e);
        }
            printf("\n");
    }
    
    return 0;
}