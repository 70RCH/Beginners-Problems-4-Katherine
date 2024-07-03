#1
password = input("Set your password:")
A = False
while not A:
    answer = input("Enter your password:")
    if answer == password:
        A = True
print ("correct!")

#1.1
1
password = input("Set your password: ")
A = False
counter = 0
while not A and counter < 3:
    answer = input("Enter your password: ")
    if answer == password:
        A = True
    else:
        counter += 1 
if A:
    print("Correct!")
else:
    print("Too many errors")


#2
n = int(input())
words = input()
for i in range(n):
    print (words)

#3
A = False
while not A:
    n = int(input("Enter a positive integer: "))
    if n > 0:
        A = True
m= []
for i in range(1, 10):
    m.append(f"n*{i}={n*i}")
print(m)

#4
A = False
while not A:
    n = int(input("Enter a number: "))
    if n <= 1:
        A = False
        print("Please enter a number greater than 1.")
    else:
        A = True
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if n == i:
                break
            if n % i == 0:
                A = False
                break
        if A:
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
print("You entered a prime number.")

#5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)