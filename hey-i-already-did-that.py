def solution(n, b):
    z = str(n)
    
    nDigits = []
    for i in z:
        nDigits.append(int(i))
    k = len(nDigits)
    outputHistory = []

    cycleLength = 0
    while cycleLength < 1:
        digits = []
        for i in z:
            digits.append(int(i))

        digitsAsc = sorted(digits)
        digitsDes = sorted(digits, reverse = True)

        x = ""
        for i in digitsDes:
            x += str(i)
        x = int(x, b)

        y = ""
        for i in digitsAsc:
            y += str(i)
        y = int(y, b)

        baseList = numToBase(x - y, b)

        z = ""
        for i in baseList:
            z += str(i)
        
        while len(z) < k:
            z = "0" + z

        if z in outputHistory:
            cycleList = outputHistory[outputHistory.index(z):]
            cycleLength = len(cycleList)
        else:
            outputHistory.append(z)

    return cycleLength

def numToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    return sorted(digits, reverse = True)