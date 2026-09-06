#include <stdio.h>

void factorial(int *n, long long *result) {
    *result = 1;

    for (int i = 1; i <= *n; i++) {
        *result *= i;
    }
}

int main() {
    int n;
    long long result;

    scanf("%d", &n);

    factorial(&n, &result);

    printf("Factorial:%lld\n", result);

    return 0;
}