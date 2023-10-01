print("4 8 15 16 23 42")

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

x = int(input())
print(x)
print(x + 1)
print(x + 2)

x = int(input())
y = int(input())
z = int(input())
print(x + y + z)

a = int(input())
print("Volume =", a * a * a)
print("Total surface area =", a * a * 6)

n = int(input())
k = int(input())
print(k // n)
print(k % n)

x = int(input())
print("The digit in the thousands position is", x // 1000)
print("The number in the hundreds position is", x // 100 % 10)
print("The digit in the tens position is", x // 10 % 10)
print("The digit in the position of units is", x % 10)

n = int(input())
if n % 2 == 1:
    print((n+1)//2)
else:
    print(n//2)

x = int(input())
if x << x == 0:
    print("Warning!!!, The result of << is 0")
else:
    print("The result of << is", x << x)

print("Please enter the first number: ")
x1 = int(input())
print("Please enter the second number: ")
x2 = int(input())
print("Please choose the operation (+, -, *, /) : ")
operation = input()
if operation == '+':
    print(x1 + x2)
elif operation == '-':
    print(x1 - x2)
elif operation == '*':
    print(x1 * x2)
elif operation == '/':
    print(x1 / x2)
