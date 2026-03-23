class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cont = 0
        for i in s[::-1]:
            if i == ' ':
                if cont == 0:
                    pass
                else:
                    break
            else:
                cont+=1
            
        return cont