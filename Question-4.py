# QUESTION 2 (STRING + HASHMAP + LOGIC)
# 🧾 Problem Statement

# Given a string, find the first non-repeating character.

# If all characters repeat → print -1
# 📥 Input Format
# Single string
# 📤 Output Format
# Print the character OR -1
# 🧪 Sample Input 1
# aabbcdeff
# ✅ Sample Output
# c
# 🧪 Sample Input 2
# aabbcc
# ✅ Sample Output
# -1

def first_non_repeating(string):
    mp = {}
    for char in string:
        mp[char] = mp.get(char, 0) + 1
    # for item, value in mp.items(): # this does not always give first non repeating 
    #     if value == 1:
    #         return item

    for char in string:
        if mp[char] == 1:
            return char
    return -1

string = input()
print(first_non_repeating(string))