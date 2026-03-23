int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) 
{
    int *ans = (int*) malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    int cont = 0;

    for (int i = 0; i < numsSize; i++)
        if (nums[i] < pivot)
            ans[cont++] = nums[i];

    for (int i = 0; i < numsSize; i++)
        if (nums[i] == pivot)
            ans[cont++] = nums[i];

    for (int i = 0; i < numsSize; i++)
        if (nums[i] > pivot)
            ans[cont++] = nums[i];

    return ans;
}