#include <stdio.h>

int main()
{   
    float price, food, vat;
    printf("summary price : ");
    scanf("%f", &price);

    food = price*100/107;
    vat = price - food;
    
    printf("food : %f\nvat : %f", food, vat);

};