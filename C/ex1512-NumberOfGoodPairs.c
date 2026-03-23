int numIdenticalPairs(int* nums, int numsSize) 
{
    int ans = 0;
    for(int i = 0; i < numsSize; i++)
        for(int j = 1 + i; j < numsSize; j++)
            if (nums[i] == nums[j])
                ans++;

    return ans;
}