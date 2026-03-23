class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ano = bin(int(date[:4])) [2:]
        mes = bin(int(date[5:7])) [2:]
        dia = bin(int(date[8:])) [2:]

        return str(ano)+'-'+str(mes)+'-'+str(dia)

        
        