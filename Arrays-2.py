# ARRAYS
# 1️⃣ Move Zeros to End
# Input:
# 8
# 4 5 0 1 9 0 5 0
# Output:
# 4 5 1 9 5 0 0 0   
def zeros_to_end(array):
    new_array = []
    count = 0
    for item in array:
        if item != 0:
            new_array.append(item)
            count += 1
    for _ in range(count, len(array)):
        new_array.append(0)
    return new_array
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))      
# print(*zeros_to_end(array)) 
    

# 2️⃣ Second Largest Element
# Input:
# 5
# 10 20 4 45 99
# Output:
# 45
def second_largest(array):
    max = -2
    second_max = -1
    for item in array:       
        if item >= max:
            second_max = max
            max = item
        if item != max and item >= second_max:
            second_max = item 
    return second_max
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))      
# print(second_largest(array)) 

# 3️⃣ Remove Duplicates (keep order)
# Input:
# 6
# 1 2 2 3 1 4
# Output:
# 1 2 3 4
def remove_duplicates(array):
    seen = set()
    new_array = []
    for item in array:
        if item not in seen:
            seen.add(item)
            new_array.append(item)
    return new_array
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))      
# print(*remove_duplicates(array)) 

# 4️⃣ Left Rotate Array (by 1)
# Input:
# 5
# 1 2 3 4 5
# Output:
# 2 3 4 5 1
# def left_rotate_array(array, rotate): # complicated
#     rotate_index = -1
#     if rotate < len(array):
#         rotate_index = rotate
#     else:
#         rotate_index = rotate - len(array)
#     new_array = []
#     for index in range(len(array)):
#         if index == rotate_index:
#             new_index = index
#             while(new_index < len(array)):
#                 new_array.append(array[new_index])
#                 new_index += 1
#             new_index = 0
#             while(new_index < index):
#                 new_array.append(array[new_index])
#                 new_index += 1
#             break
#     return new_array
def left_rotate_array(array, rotate): 
    rotate_index = rotate % len(array)
    new_array = []
    new_index = rotate_index
    while(new_index < len(array)):
        new_array.append(array[new_index])
        new_index += 1
    new_index = 0
    while(new_index < rotate_index):
        new_array.append(array[new_index])
        new_index += 1
    return new_array
# rotate = int(input())
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))      
# print(*left_rotate_array(array, rotate)) 



# 5️⃣ Find Missing Number
# Input:
# 5
# 1 2 4 5
# Output:
# 3
# def find_max(array):
#     max = array[0]
#     for item in array:
#         if item > max:
#             max = item
#     return max

# def find_min(array):
#     min = array[0]
#     for item in array:
#         if item < min:
#             min = item
#     return min

# def find_missing(array):
#     max = find_max(array)
#     min = find_min(array)
#     for index in range(min,max+1):
#         if index not in array:
#             return index
#     return -1
def find_missing(array, n):
    for index in range(1, n+1): 
        if index != array[index-1]:
            return index
    return -1
# n = int(input())
# array = []
# for _ in range(n-1):
#     array.append(int(input()))  
# print(find_missing(array, n))

# 6️⃣ Leaders in Array
# 👉 (Element greater than all elements to its right)
# Input:
# 6
# 16 17 4 3 5 2
# Output:
# 17 5 2
# def check_max(array, element_index):
#     for index in range(element_index, len(array)):
#         if array[element_index] < array[index]:
#             return False
#     return True
            
# def leaders_in_array(array): # not optimal but correct
#     leaders = []
#     for index in range(len(array)):
#         if check_max(array, index):
#             leaders.append(array[index])
#     return leaders

def leaders_in_array(array):
    if not array:
        return []
    leaders = []
    max_right = array[-1]
    leaders.append(max_right)
    for index in range(len(array)-2, -1, -1):
        if array[index] > max_right:
            max_right = array[index]
            leaders.append(max_right)
    return leaders[::-1]
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input()))  
# print(*leaders_in_array(array))

# 7️⃣ Kadane’s Algorithm (Max Subarray Sum)
# Input:
# 8
# -2 -3 4 -1 -2 1 5 -3
# Output:
# 7
# 👉 Subarray: [4, -1, -2, 1, 5]
# def max_subarray_sum(array):
#     max_sum = array[0]
#     for index in range(len(array)):
#         curr_sum = 0
#         for pos in range(index, len(array)):
#             curr_sum += array[pos]
#             max_sum = max(max_sum, curr_sum)
#     return max_sum
def kadanes_algorithm(array):
    max_sum = array[0]
    curr_sum = array[0]
    for index in range(1, len(array)):
        curr_sum = max(array[index], array[index]+curr_sum)
        max_sum = max(max_sum, curr_sum)
    return max_sum
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(int(input())) 
# print(kadanes_algorithm(array))

# 8️⃣ Merge Two Sorted Arrays
# Input:
# Array1: 1 3 5
# Array2: 2 4 6
# Output:
# 1 2 3 4 5 6

def merge_arrays(array1, array2): # wrong
    return array1 + array2
print(*merge_arrays([1,2], [3,4,5]))