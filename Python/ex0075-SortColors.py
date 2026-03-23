class Solution:
    def sortColors(self, nums: List[int]) -> None:
        tam = len(nums)-1
        i, f = 0, tam
        j = 0
        while j <= f:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
                j+=1
            elif nums[j] == 2:
                nums[j], nums[f] = nums[f], nums[j]
                f-=1
            else:
                j+=1
