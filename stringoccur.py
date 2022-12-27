# Write a Python program to compute following operations on String: 
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not
#  d) To display index of first appearance of the substring 
#  e) To count the occurrences of each word in a given string

def length(string):

    counter = 0
    for i in string:
        counter += 1

    return counter

#function for splitting words in a string
def split_words(string):

    word_list = []
    temp_str = ""

    for i in range (length(string)):
        if string[i] != " ":
            temp_str += string[i]
        else:
            word_list.append(temp_str)
            temp_str = ""
    word_list.append(temp_str)

    return word_list

#function to find the longest word in a string
def longest(string):

    word_list = split_words(string)
    max = -1

    for i in word_list:
        if length(i) > max:
            max = length(i)
            longest_word = i

    return longest_word

#function to check if string is palindrome
def is_palindrome(string):

    reversed = ""

    for i in range(length(string)-1, -1, -1):
        reversed += string[i]

    if reversed == string:
        return True
    else:
        return False

#function to check for given substring in string
def check_substring(string, sub):

    wall = length(string) - length(sub)

    index = -1
    counter = 0

    for i in range (wall):
        for j in range(length(sub)):
            if string[i+j] == sub[j]:
                counter += 1
            else:
                counter = 0
                break
        if counter == length(sub):
            index = i
            
    return index

#function to count the frequency of every word in the string
def occ_words(string):

    a = split_words(string)
    b = {}

    for i in a:
        if i not in b.keys():
            b[i] = 1
        else:
            b[i] += 1

    return b

#function to find frequency of a certain character in the string
def occ_char(string, ch):

    counter = 0

    for i in string:
        if i == ch:
            counter += 1

    return counter

#taking the string as input
inpStr = str(input("\nEnter the string: "))

#finding the longest word in the string
print("\n\nThe longest word in string is: ", longest(inpStr))

#finding frequency of a certain character in string
ch = input("\n\nEnter the character to find frequency: ")
print("The character ", ch, " has occured ", occ_char(inpStr, ch), " times in the string")

#check whether given string is palindrome 
if is_palindrome(inpStr):
    print("\n\nString is a palindrome")
else:
    print("\n\nString is not a palindrome")

#find index of first appearance of substring
substring = str(input("\n\nEnter substring to find index: "))
index = check_substring(inpStr, substring)
if index == -1:
    print("Substring doesn't exist in string")
else:
    print("Substring is present at index ", index)

#count the occurances of every word in string
print("\n\nCounts of words occured in the string: ")
print(occ_words(inpStr))
