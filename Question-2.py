# QUESTION 2 (MODERATE)
# 🧾 Problem Statement

# A special series is defined as follows:

# Odd positions → Fibonacci sequence
# Even positions → Prime numbers

# Series:

# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, ...

# 👉 Write a program to find the Nth term of this series.

# 📥 Input Format
# Single integer N
# 📤 Output Format
# Print the Nth term
# 📌 Constraints
# 1 ≤ N ≤ 30
# 🧪 Sample Input
# 14
# ✅ Sample Output
# 17

def get_prime(n):
    primes = []
    for index in range(2, n+2):
        num = 2
        flag = True
        while(num * num <= index):
            if index % num == 0:
                flag = False
                break
            num += 1
        if flag == True:
            primes.append(index)
    return primes

def get_fibonacci(n):
    prev, curr = 1, 1
    fibonacci = []
    for index in range(0, n):
        fibonacci.append(prev)
        next = prev + curr 
        prev = curr
        curr = next
    return fibonacci

def fibonacci_prime_series(n):
    if n % 2 == 0:
        return get_prime(int(n/2))[-1]
    else:
        return get_fibonacci(int((n/2))+1)[-1]
    
    
print(fibonacci_prime_series(int(input())))