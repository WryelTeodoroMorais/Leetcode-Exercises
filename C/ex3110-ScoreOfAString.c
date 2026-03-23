int scoreOfString(char* s) 
{
    int count = 0;
    for (int i = 1; i < strlen(s); i++)
        count += abs(s[i - 1] - s[i]);
        
    return count;
}