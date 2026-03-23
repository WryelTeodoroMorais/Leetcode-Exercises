class Solution:
    def intToRoman(self, num: int) -> str:
            M = num // 1000
            aux = num % 1000
            result = 'M' * M
            if aux // 900 == 1:
                result += 'CM'
                aux = aux % 900
            else:
                D = aux // 500
                aux = aux % 500
                result += 'D' * D
                if aux // 400 == 1:
                    result += 'CD'
                    aux = aux % 400
            C = aux // 100
            aux = aux % 100
            result += 'C' * C
            if aux // 90 == 1:
                result += 'XC'
                aux = aux % 90
            else:
                L = aux // 50
                aux = aux % 50
                result += 'L' * L
                if aux // 40 == 1:
                    result += 'XL'
                    aux = aux % 40
            X = aux // 10
            aux = aux % 10
            result += 'X' * X
            if aux // 9 == 1:
                result += 'IX'
                aux = aux % 9
            else:
                V = aux // 5
                aux = aux % 5
                result += 'V' * V
            if aux // 4 == 1:
                result += 'IV'
            else:
                result += 'I' * aux
            
            return result
