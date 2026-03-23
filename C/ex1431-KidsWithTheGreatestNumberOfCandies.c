bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) 
{
    *returnSize = candiesSize;
    bool *ans = (bool*) malloc(candiesSize * sizeof(bool));
    int maior = 0;

    for(int i = 0; i < candiesSize; i++)
        if (candies[i] > maior)
            maior = candies[i];

    for(int i = 0; i < candiesSize; i++)
    {
        if (candies[i] + extraCandies >= maior)
            ans[i] = true;
        else
            ans[i] = false;
    }

    return ans;
}