#include <stdio.h>

int main()
{   
    float m, c;
    int e;

    printf("Milk: "); scanf("%f", &m);
    printf("Coffee: "); scanf("%f", &c);

    e = m*c*c;
    printf("%d", e);
};