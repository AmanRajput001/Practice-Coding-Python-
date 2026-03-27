# STRINGS
# 1️⃣ Palindrome Check
# Input:
# racecar

# Output:
# True
# Input:
# hello
# Output:
# False
def is_palindrome(string):
    # return string[::-1] == string # it will take extra space
    start = 0
    end = len(string) - 1
    while(start <= end):
        if(string[start] != string[end]):
            return False        
        start += 1
        end -= 1
    return True

# 2️⃣ Anagram Check
# Input:
# listen
# silent
# Output:
# True
# Input:
# hello
# world
# Output:
# False
def is_anagram(string1, string2):
    mp = dict()
    for char in string1:
        mp[char] = mp.get(char, 0) + 1
    for char in string2:
        mp[char] = mp.get(char, 0) - 1
        if mp[char] == -1:
            return False
    return True

# 3️⃣ Reverse Words (characters inside words)
# Input:
# Apple is good

# Output:
# elppA si doog
def reverse_word(word):
    rev = ""
    for index in range(len(word) - 1, -1, -1):
        rev += word[index]
    return rev
def reverse_word_sentence(string):
    new_string = ""
    word = ""
    for char in string:
        if char == " ":
            rev = reverse_word(word) + " "
            new_string += rev
            word = ""
        else:
            word += char
    # for last word    
    rev = reverse_word(word) + " "
    new_string += rev   
    return new_string
# def reverse_word_sentence(string): # uses inbuilt methods
#     words = string.split(" ") # list
#     for index in range(len(words)):
#         words[index] = words[index][::-1]
#     return " ".join(words)

# string = input()
# print(reverse_word_sentence(string))

# 4️⃣ First Non-Repeating Character
# Input:
# aabbcdeff

# Output:
# c
# Input:
# aabbcc

# Output:
# -1
def first_non_repeating_char(string):
    mp = {}
    for char in string:
        mp[char] = mp.get(char, 0) + 1
    for char in string:
        if mp[char] == 1:
            return char
    return -1

# 5️⃣ Count Vowels & Consonants
# Input:
# Apple is good

# Output:
# Vowels: 6
# Consonants: 7
def count_vowels_consonants(string):
    count_vowels, count_consonants = 0, 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count_vowels += 1
        elif char.isalpha():
            count_consonants += 1
    return [count_vowels, count_consonants]

# 6️⃣ Remove Duplicates from String
# Input:
# aabbccdde

# Output:
# abcde
# Input:
# programming
# Output:
# progamin
def remove_duplicates(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

# 7️⃣ String Rotation Check
# Input:
# abcd
# cdab
# Output:
# True
# Input:
# abcd
# acbd
# Output:
# False
# def rotation_check(string1, string2): #complicated
#     if len(string1) != len(string2):
#         return False
#     first, second, pos = 0, 0, 0
#     while(True):
#         print(first, second, pos)
#         if second == len(string2) and pos == len(string2):
#             return True
#         elif second != len(string2) and first == len(string1):
#             first = 0
#         elif second == len(string2) and pos != len(string2):
#             return False
#         elif string1[first] == string2[second]:
#             first += 1
#             second += 1
#             pos += 1
#         else:
#             first += 1
#             pos = 0

def rotation_check(string1, string2):
    if len(string1) != len(string2):
        return False
    return string2 in (string1+string1)

string1 = input()
string2 = input()
print(rotation_check(string1, string2))

            