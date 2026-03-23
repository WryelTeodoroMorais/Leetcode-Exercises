class Solution:
    def myAtoi(self, s: str) -> int:
        result = []
        sinal = 0
        flag = -1
        for i in s:
            if i.isdigit():
                result.append(i)
            else:
                if i == ' ' and result == [] and flag == -1:
                    pass
                elif i == '+' and result == [] and flag == -1:
                    flag = 0
                elif (i == '-') and result == [] and flag == -1:
                    flag = 0
                    sinal = 1
                else:
                    break

        final = ("".join(result))

        if final == '':
            return 0
        
        resp = int(final)
        if resp > (pow(2,31) - 1) and sinal == 0:
            return pow(2,31) - 1
        elif resp > (pow(2,31)) and sinal == 1:
            return -pow(2,31)

        if sinal == 0:
            return resp
        else:
            return -resp