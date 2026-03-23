int* shuffle(int* nums, int numsSize, int n, int* returnSize)
{
    *returnSize = numsSize;
    int *ans = (int*)malloc(numsSize * sizeof(int)), j = 0;
    for (int i = 0; i < n; i++)
    {
        ans[j++] = nums[i];
        ans[j++] = nums[i + n];
    }

    return ans;
}