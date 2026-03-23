int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) 
{
    *returnSize = 2;
    int *ans = (int*)malloc(2 * sizeof(int)), cont2 = 0;
    
    for (int i = 0; i < numsSize; i++)
    {
        if (cont2 == 2)
            break;
            
        for(int j = i + 1; j < numsSize; j++)
            if (nums[i] == (nums[j]))
            {
                ans[cont2] = nums[i];
                cont2++;
            }
    }

    return ans;
}