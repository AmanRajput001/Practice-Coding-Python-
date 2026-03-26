# Armstrong number = Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 
def check_armstrong(num):
    sum = 0
    for digit in num:
        digit = int(digit)
        cube = digit * digit * digit
        sum += cube
    return int(num) == sum
# num = input()
# print(check_armstrong(num))

# Prime check
def check_prime(num):
    if num <= 1:
        return False
    i = 2
    while(i * i <= num):
        if num % i == 0:
            return False
        i += 1
    return True
# num = int(input())
# print(check_prime(num))

# Fibonacci series
def get_fibonacci(n):
    prev, curr = 1, 1
    array = []
    for _ in range(n):
        array.append(prev)
        next = prev + curr
        prev = curr
        curr = next
    return array
# n = int(input())
# print(*get_fibonacci(n))

# GCD / LCM
# Happy number 
def check_happy_number(num):    
    occured = [num]
    while(True):
        sum = 0
        for digit in num:
            digit = int(digit)
            sqr = digit * digit
            sum += sqr
        if sum in occured:
            return False
        elif sum == 1:
            return True
        else:
            occured.append(sum)
        num = str(sum)
num = input()
print(check_happy_number(num))