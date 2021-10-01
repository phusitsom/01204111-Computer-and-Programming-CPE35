#include <stdio.h>

int main()
{   
    int money, son;

    printf("Money: "); scanf("%d", &money);
    printf("Son: "); scanf("%d", &son);

    printf("%d %d", money/son, money%son);
};