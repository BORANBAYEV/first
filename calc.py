def calc(num1, num2, oper):
    print(num1, num2, oper)

    if oper == "//":
        return num1 // num2

    if oper == "/":
        if num2 !=0:
            return num1 / num2
        else:
            print("вы ввели 0")
            return 0

    if oper == "**":
        return num1 ** num2

    if oper == "*":
        return num1 * num2

    if oper == "+":
        return num1 + num2

    if oper == "-":
        return num1 - num2

    if oper == "%":
        return num1 % num2

    import math
    num = 25
    sqrt = math.sqrt(num)
    print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))



result = calc(12, 11, "sqrt")
print(result)

result = calc(12, 11, "**")
print(result)

result = calc(12, 11, "/")
print(result)

result = calc(12, 11, "//")
print(result)
