A = int(input("Минимум сна: "))
B = int(input("Максимум сна: "))
H = int(input("Текущий сон: "))

if A <= H <= B:
    print("Это нормально")
elif H < A:
    print("Недосып")
else:
    print("Пересып")

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")


