# 🔴 QUESTION 1 (EASY–MODERATE)
# 🧾 Problem Statement

# A chocolate factory is packing chocolates into packets. Each packet is represented as an integer array where:

# 0 represents an empty packet
# Non-zero values represent chocolates

# Your task is to move all empty packets (0s) to the end of the array while maintaining the order of non-zero elements.

# 📥 Input Format
# First line: Integer N (size of array)
# Next N lines: Elements of array

# 📤 Output Format
# Print the modified array (space-separated)

# 📌 Constraints
# 1 ≤ N ≤ 100
# -100 ≤ arr[i] ≤ 100

# 🧪 Sample Input
# 8
# 4
# 5
# 0
# 1
# 9
# 0
# 5
# 0
# ✅ Sample Output
# 4 5 1 9 5 0 0 0

# def move_zeros_to_end(size, org_array):
#     array = org_array
#     end = size
#     index = 0
#     while(index < end):
#         if array[index] == 0:
#             for i in range(index, end-1):
#                 array[i] = array[i+1] # shift
#             array[end-1] = 0
#             end -= 1
#         else:
#             index += 1
#     print(array)

def move_zeros_to_end(size, array):
    pos = 0
    for index in range(len(array)):
        if array[index] != 0:
            array[pos] = array[index]
            pos += 1
    
    for index in range(pos, len(array)):
        array[index] = 0

    return array

size = int(input())
array = []
for _ in range(size):
    array.append(int(input()))
print(*move_zeros_to_end(size, array))