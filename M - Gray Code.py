def generateGrayCode(n):
    if n == 1:
        return ["0","1"]
    else:
        prevGrayCode = generateGrayCode(n-1)
        revPrevGrayCode = prevGrayCode[::-1]
        Size = len(prevGrayCode)
        for i in range(Size):
            appendedZero = "0" + prevGrayCode[i]
            prevGrayCode[i] = "1"+ revPrevGrayCode[i]
            prevGrayCode.append(appendedZero)

        return prevGrayCode

for code in generateGrayCode(int(input())):
    print(code)