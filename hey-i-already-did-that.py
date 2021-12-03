def solution(n, b):
    z = n
    cycle = 0
    nDigits = []
    for i in str(z):
        nDigits.append(int(i))
    k = len(nDigits)

    while str(n) != z or cycle < 1:
        digits = []
        for i in str(z):
            digits.append(int(i))

        digitsAsc = sorted(digits)
        digitsDes = sorted(digits, reverse = True)

        x = ""
        for i in digitsDes:
            x += str(i)
        x = int(x)

        y = ""
        for i in digitsAsc:
            y += str(i)
        y = int(y)

        z = x - y
        z = str(z)
        while len(z) < k:
            z = "0" + z
        print(z, str(n))
        cycle += 1
    print(cycle)

solution(1211, 10)