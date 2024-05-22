for num in range(3):
    password=input("Enter Password:")
    if password == "abcd":
        print("correct password")
        exit()
print("locked")

num = int(input("Enter a number: "))
name = input("Enter your name: ")

for _ in range(num):
    print(name)


while True:
    num = input("Enter a positive integer: ")
    if num.isdigit() and int(num) > 0:
        num = int(num)
        for i in range(1, 13):
            print(f"{num} x {i} = {num*i}")
        break
    else:
        print("Not a positive integer.")

        
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter an integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    

for num in range(1, 101):
    try:
        input_num = int(input(f"Enter {num}: "))
        if input_num != num:
            print(f"You entered {input_num}, but expected {num}. Exiting the loop.")
            break
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
    except ValueError:
        print("You entered a non-integer value. Exiting the loop.")
        break
