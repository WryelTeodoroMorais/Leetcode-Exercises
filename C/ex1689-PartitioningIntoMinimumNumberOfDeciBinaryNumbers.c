int minPartitions(char* n) 
{
    char aux = '0';
    
    for(int i = 0; i < strlen(n); i++)
        if (n[i] > aux)
            aux = n[i];

    return aux - '0';
}