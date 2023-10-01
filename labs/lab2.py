# task1
num = int(input("Enter a four-digit number: "))
if 1000 <= num <= 9999:
    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    ones = num % 10
  
    if thousands + ones == abs(tens - hundreds):
        print("YES")
    else:
        print("NO")
else:
    print("Invalid input. Please enter a four-digit number.")




# task2
age = int(input("Enter your age: "))
if age >= 18:
    print("Access allowed")
else:
    print("Access denied")


# task3

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num2 - num1 == num3 - num2:
    print("YES")
else:
    print("NO")

# task4

x1, y1, x2, y2 = map(int, input().split())

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

#task5

x1, y1, x2, y2 = map(int, input().split())


if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")

#task6

a = int(input())
b = int(input())
c = int(input())


average = (a + b + c - min(a, b, c) - max(a, b, c)) / 1.0

print(average)

#task7

month = int(input("Enter the month number (1-12): "))

if month == 2:
    days = 28
elif month in {4, 6, 9, 11}:
    days = 30
else:
    days = 31

print(f"Number of days in month {month}: {days}")

#task8

weight = int(input("Enter the boxer's weight (in kg): "))


if weight <= 60:
    category = "Lightweight"
elif weight <= 64:
    category = "First Welterweight"
elif weight <= 69:
    category = "Welterweight"
else:
    category = "Unknown"

print(f"The boxer will compete in the {category} category.")

#task9

password = input("Enter your password: ")
confirmation = input("Confirm your password: ")


if password == confirmation:
    print("Password accepted")
else:
    print("Password not accepted")

#task10

number = int(input("Enter a number: "))


if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#task11

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if num1 < num2:
    smallest = num1
else:
    smallest = num2


print(f"The smallest number is: {smallest}")


#task12

age = int(input("Enter your age: "))


if age <= 13:
    age_group = "childhood"
elif age >= 14 and age <= 24:
    age_group = "youth"
elif age >= 25 and age <= 59:
    age_group = "maturity"
else:
    age_group = "old age"


print(f"You belong to the {age_group} age group.")



#task13

a = int(input("Enter the length of side A: "))
b = int(input("Enter the length of side B: "))
c = int(input("Enter the length of side C: "))


if a == b == c:
    triangle_type = "Equilateral"
elif a == b or b == c or a == c:
    triangle_type = "Isosceles"
else:
    triangle_type = "Versatile"


print(f"The triangle is {triangle_type}.")

