class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def Inicio():
            inicio, fim = 0, len(nums) -1
            pos = -1
            while inicio <= fim:
                meio = (inicio + fim) // 2
                if nums[meio] < target:
                    inicio = meio + 1
                else:
                    fim = meio - 1
                if nums[meio] == target:
                    pos = meio
            
            return pos
            
        def Fim():
            inicio, fim = 0, len(nums) -1
            pos = -1
            while inicio <= fim:
                meio = (inicio + fim) // 2
                if nums[meio] <= target:
                    inicio = meio + 1
                else:
                    fim = meio - 1
                if nums[meio] == target:
                    pos = meio
            
            return pos

        return Inicio(), Fim()
            