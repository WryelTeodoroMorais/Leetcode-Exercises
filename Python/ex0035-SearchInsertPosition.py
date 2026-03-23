class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        inicio, fim = 0, len(nums) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if target == nums[meio]:
                return meio
            elif target < nums[meio]:
                fim = meio-1
            else:
                inicio = meio+1

        return inicio