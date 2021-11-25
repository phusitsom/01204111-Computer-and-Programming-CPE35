#include <stdio.h>
int isPrime(int n);

int main() 
{
  int n, i;
  printf("Enter a positive integer: ");
  scanf("%d", &n);

  for (i = 2; i <= n / 2; ++i)
    if (isPrime(i) && isPrime(n - i))
        printf("%d = %d + %d\n", n, i, n - i);
  return 0;
}

int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i=2; i*i<=n; ++i) {
        if (n % i == 0) return 0;
    }
    return 1;
}