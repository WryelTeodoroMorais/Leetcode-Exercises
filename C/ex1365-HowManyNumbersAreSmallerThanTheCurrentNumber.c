int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) 
{
    *returnSize = numsSize;
    int *ans = (int*) malloc (sizeof(int) * numsSize);
    int cont;

    for (int i = 0; i < numsSize; i++)
    {
        cont = 0;
        for(int j = 0; j < numsSize; j++)
        {
            if (nums[i] > nums[j])
                cont++;
        }
        ans[i] = cont;
    }

    return ans;
}