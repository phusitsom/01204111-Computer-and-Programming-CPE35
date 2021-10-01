#include <stdio.h>

int main()
{
    char name[256];
    printf("Please tell me your name : ");
    scanf("%s", &name);
    printf("Hello, teacher and lovely TA..\nMy name is %s\n%s is CPE#35 student..\n%s's favorite is Python.\nTHANKS", name, name, name);

}