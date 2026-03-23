char* defangIPaddr(char * address)
{
    int cont = 0, aux = 0;
    int tam = strlen(address);

    for (int i = 0; i < tam; i++)
        if (address[i] == '.')
            aux++;

    char *ans = (char*) malloc(tam * sizeof(char) + aux * 2 + 1);
    for (int i = 0; i < tam; i++)
    {
        if (address[i] == '.')
        {
            ans[cont++] = '[';
            ans[cont++] = '.';
            ans[cont++] = ']';
        } 
        else
            ans[cont++] = address[i];
    }

    ans[cont] = '\0';
    return ans;
}