# QUESTION 1 (ARRAY + GREEDY + TRICK)
# 🧾 Problem

# Given an array of integers, you can perform operations:

# Choose any element and decrease it by 1

# Find the minimum number of operations required to make the array strictly increasing

# 📥 Input
# 5
# 1 1 1 1 1
# 📤 Output
# 10

def strictly_increasing(array):
    index = len(array) - 1
    operation = 0
    while(index > 0):
        if array[index-1] >= array[index]: 
            operation += 1
            array[index] -= operation
        index -= 1
    return operation
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
print(strictly_increasing(array))