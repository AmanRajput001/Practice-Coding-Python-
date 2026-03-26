# Write a program to check whether a string is a palindrome.
def check_palindrome(string):
    # return string.lower() == string[::-1].lower()
    string = string.lower()
    start = 0
    end = len(string) - 1
    while(start <= end):
        if string[start] is not string[end]:
            return False
        start = start + 1
        end = end - 1
    return True
# print(check_palindrome("ABobA"))

#--------------------------------------------------------------------------------#

# Write a program to reverse words in a sentence without using library methods.
# def reverse_words(word):
#     return word[::-1]
def reverse_words(word):
    rev = ""
    for i in range(len(word) - 1, -1, -1):
        rev += word[i]
    return rev

def reverse_sentence(string):
    revString = ""
    word = ""
    for item in string:
        if item == " ":
            revString = revString + reverse_words(word) + " "
            word = ""
        else:
            word = word + item 
    revString = revString + reverse_words(word) + " "
    return revString
# print(reverse_sentence("Apple is good for body."))

#--------------------------------------------------------------------------------#

# Write a program to count vowels and consonants in a string.
def count_vowels_consonants(string):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    count_consonents = 0
    for item in string:
        if item in vowels:
            count_vowels = count_vowels + 1
        elif item.isalpha():
            count_consonents = count_consonents + 1
    return count_vowels, count_consonents
# print(count_vowels_consonants("Apple is good for body."))

#--------------------------------------------------------------------------------#

# Write a program to check whether two strings are anagrams.
def check_anagrams(string1, string2):
    if len(string1) is not len(string2):
        return False

    string1 = string1.lower()
    string2 = string2.lower()

    mp1 = {}
    for item in string1:
        mp1[item] = mp1.get(item, 0) + 1
    
    for item in string2:
        mp1[item] = mp1.get(item, 0) - 1
        if mp1[item] < 0:
            return False
    return True
# print(check_anagrams("SELFf", "ELFSa"))

#--------------------------------------------------------------------------------#

# Write a program to convert a string into lowercase.
def to_lowercase(string):
    return string.lower()
print(to_lowercase("ABCDabcd"))
