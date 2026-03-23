int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) 
{
    int *ans = (int*)malloc(wordsSize * sizeof(int)), cont = 0;
    for (int i = 0; i < wordsSize; i++)
    {
        for (int j = 0; words[i][j] != '\0' ; j++)
        {
            if (words[i][j] == x)
            {
                ans[cont++] = i;
                break;
            }
        }
    }

    *returnSize = cont;
    ans = (int*)realloc(ans, cont * sizeof(int));
    return ans;
}