class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tam = len(digits) - 1
        while tam >= 0:
            if digits[tam] < 9:
                digits[tam]+=1
                return digits
            digits[tam] = 0
            tam-=1
            
        return [1] + digits
            