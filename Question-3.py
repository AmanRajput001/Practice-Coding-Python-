# QUESTION 1 (ARRAY + LOGIC TWIST)
# 🧾 Problem Statement

# You are given an array of integers.
# Your task is to rearrange the array such that positive and negative numbers alternate, while maintaining their relative order.

# If extra positives or negatives remain, place them at the end.
# 📥 Input Format
# First line: Integer N
# Next N lines: Elements of array
# 📤 Output Format
# Print rearranged array (space-separated)
# 🧪 Sample Input
# 7
# 1
# 2
# -3
# -4
# 5
# -6
# 7
# ✅ Sample Output
# 1 -3 2 -4 5 -6 7

def positive_negative_arrangement(array):
    positive = []
    negative = []

    for item in array:
        if item < 0:
            negative.append(item)
        else:
            positive.append(item)
    i = 0
    new_array = []
    while((i < len(positive) and i < len(negative))):
        new_array.append(positive[i])
        new_array.append(negative[i])
        i += 1
    
    while(i < len(positive)):
        new_array.append(positive[i])
        i += 1
    while(i < len(negative)):
        new_array.append(negative[i])
        i += 1
    return new_array

n = int(input())
array = []
for _ in range(0,n):
    array.append(int(input()))
print(*positive_negative_arrangement(array))