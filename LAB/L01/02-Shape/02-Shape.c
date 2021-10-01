#include <stdio.h>

int main()
{
    float w, l, a, p;

    printf("width : ");
    scanf("%f",&w);

    printf("length : ");
    scanf("%f",&l);

    printf("area :%f\nperimeter :%f",w*l, 2*(w+l));
};