int* transformArray(int* nums, int numsSize, int* returnSize) 
{
    *returnSize = numsSize;
    int cont0 = 0, cont1 = 0;
    int *ans = (int*) malloc (numsSize * sizeof(int));
    for(int i = 0; i < numsSize; i++)
    {
        if (nums[i] % 2 == 0)
            cont0++;
        else
            cont1++;
    }

    for(int i = 0; i < cont0; i++)
         ans[i] = 0;
    for(int i = cont0; i < cont1 + cont0; i++)
         ans[i] = 1;

    return ans;
}
