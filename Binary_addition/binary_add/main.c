#include <stdio.h>
#include <stdlib.h>
#include<string.h>

char *binary_add(unsigned a, unsigned b, char *binary)
{
    char one ='1';
    char zero = '0';
    char result[] = "";
    unsigned long long sum = a+b;
    printf("sum of %d and %d is %lld \n", a,b, sum);
    while(sum >=1)
    {
        if ( (sum%2) ==1)
        {
            printf("1");
           strncat(result, &one,1);
        }
        else
        {
            printf("0");
            strncat(result, &zero,1);
        }
        sum = sum>>1;

    }
    //
    printf("\n Loop ended\n");
    *binary = result;
    return *binary;
}

int main()
{
    printf("binary_add(1,2) --> %c\n", *binary_add(1,2, '\0'));
    printf("binary_add(51, 12) --> %c\n", *binary_add(1,2, '\0'));
    printf("binary_add(100, 0) --> %c\n", *binary_add(1,2, '\0'));
    printf("binary_add(0, 0) --> %c\n", *binary_add(1,2, '\0'));
    return 0;
}
