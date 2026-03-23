char* interpret(char* command)
{
    int len = strlen(command);
    char *ans = (char*) malloc(len * sizeof(char) + 1);
    int aux = 0;

    for(int i = 0; i < len; i++)
    {
        if (command[i] == 'G')
        {
            ans[aux] = 'G';
            aux++;
        }
        else if (command[i] == '(' && command[i+1] == ')')
        {
            ans[aux] = 'o';
            aux++;
            i++;
        }
        else
        {
            ans[aux] = 'a';
            ans[aux+1] = 'l';
            aux+=2;
            i+=3;
        }
    }

    ans[aux] = '\0';
    return ans;
}