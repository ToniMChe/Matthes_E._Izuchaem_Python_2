"""
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (p * (p-a) * (p - b) * (p - c)) ** (1/2)
print(S)


a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a:
    print("True")
else:
    print("False")


number_1 = float(input())
number_2 = float(input())
operation = input()
if number_2 == 0 and (operation == "mod" or operation == "div" or operation == "/"):
    print("Деление на 0!")
elif operation == "mod":
    print(number_1 % number_2)
elif operation == "pow":
    print(number_1 ** number_2)
elif operation == "div":
    print(number_1 // number_2)
elif operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "/":
    print(number_1 / number_2)
elif operation == "*":
    print(number_1 * number_2)

figure = input()
if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    print(S)
elif figure == "прямоугольник":
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
else:
    r = float(input())
    S = 3.14 * r * r
    print(S)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 >= number_2 and number_1 >= number_3:
    first = number_1
    if number_2 >= number_3:
        second = number_2
        third = number_3
    else:
        second = number_3
        third = number_2
elif number_2 >= number_1 and number_2 >= number_3:
    first = number_2
    if number_1 >= number_3:
        second = number_1
        third = number_3
    else:
        second = number_3
        third = number_1
else:
    first = number_3
    if number_1 >= number_2:
        second = number_1
        third = number_2
    else:
        second = number_2
        third = number_1

print(first)
print(third)
print(second)

n = int(input())
i = 0
if n > 10:
    i = n % 10
elif n > 100:
    i = (n % 100) % 10
else:
    i = n
if (i == 0 or 5 <= i <= 9) or 10 <= n % 100 <= 20:
    print(str(n) + " программистов")
elif i == 1:
    print(str(n) + " программист")
elif 2 <= i <= 4:
    print(str(n) + " программиста")"""

n = str(input())
n_1 = n[0]
n_2 = n[1]
n_3 = n[2]
n_4 = n[3]
n_5 = n[4]
n_6 = n[5]
if int(n_1) + int(n_2) + int(n_3) == int(n_4) + int(n_5) + int(n_6):
    print("Счастливый")
else:
    print("Обычный")