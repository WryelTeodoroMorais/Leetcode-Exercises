int minimumOperations(int* nums, int numsSize) 
{
    int oper = 0;
    
    for (int i = 0; i < numsSize; i++)
        if (nums[i] % 3 != 0)
            oper += 1;

    return oper;
}