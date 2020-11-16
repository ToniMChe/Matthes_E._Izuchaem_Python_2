a = int(input())
print(a > 0)

print(a >= 10 and a < 100)

a1, a2, a3 = False, True, False
print(not a1 or a2 and a3)

print(True or a2 and a3)
print(True or False)

x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

a = True
b = False
print(a and b or not a and not b)
