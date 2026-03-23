#include <string.h>

int reverseDegree(char* s) 
{
    int soma = 0;

    for (int i = 0; i < strlen(s); i++)
        soma += (26 - (s[i] - 'a')) * (i+1);

    return soma;
}