 #Python Basics - Module 01

# 1. Variables
name = "Student"
age = 20
print("Name:", name)
print("Age:", age)

# 2. List
numbers = [10, 20, 30, 40]
print("Numbers:", numbers)

# 3. Loop
for num in numbers:
    print(num)

# 4. Function
def greet():
    print("Welcome to Python Internship")

greet()

#sum of two numbers
a = 10
b = 20
sum = a + b
print("Sum =", sum)

#even or odd
num=10
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")


#largest number
a=25
b=20
if a>b:
    print("A is largest")
else:
    print("B is largest")

#multiplication table
num=5
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#sum of numbers using loop
total = 0
for i in range(1, 6):
    total = total + i
print("Sum =", total)

#factorial of a number
num = 5
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)

#reverse a number
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse =", rev)

#palindrome number
num = 121
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#largest number in a list
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest =", largest)

#sum of list elements
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest =", largest)

#create and call a function
def greet():
    print("Welcome to Python")
    greet()

#count even and odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even count =", even)
print("Odd count =", odd)




