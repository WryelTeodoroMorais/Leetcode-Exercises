int countConsistentStrings(char * allowed, char ** words, int wordsSize)
{
    int busca = wordsSize;

    for (int i = 0; i < wordsSize; i++)
        for(int j = 0; words[i][j]; j++)
            if (strchr(allowed, words[i][j]) == NULL)
            {
                busca--;
                break;
            }

    return busca;
}