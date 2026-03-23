int* minOperations(char* boxes, int* returnSize) 
{
    *returnSize = strlen(boxes);
    int *ans = (int*) calloc (*returnSize, sizeof(int));
    for (int i = 0; i < *returnSize; i++)
    {
        for (int j = 0; j < *returnSize; j++)
        {
            if (boxes[j] == '1' && i != j)
                ans[i]+= abs(j - i);
        }
    }

    return ans;
}