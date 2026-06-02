from re import findall,sub
s1="the theory of relativity"
# lst=[]
# for i in s1:
#     if i in 'tT':
#         lst.append(i)
# print(lst)

# lst=[]
# for i in s1.split():
#     if i == 'the':
#         lst.append(i)
# print(lst)
# print(findall('the',s1))


# s2="The dragging belly indicates your cat is too fat"
# print(findall('cat',s2))

# s3='python and java are object oriented'
# print(findall("python",s3))

# s4='hello how are you doing anna'
# print(findall("anna",s4))

# s5='hello how are you doing anna, aeiou'
# print(findall('aeiou',s5))
# --------------------------------------------------------------------------
# Matches with both "Smith" and "smith"
# s6='Smith and blacksmith'
# print(findall("[Ss]mith",s6))

# Matches "separate" or "saperate"

# Matches "grey" and "gray"

# Match any one character in the character set (either a, e, i, o, u)
# s7='hello how are you doing anna'
# print(findall('[aeiou]',s7))

# Match either a, b, c, d

# Matching any number between 0-9
##s8='The cost of the book is Rs.100'
##print(findall('[0-9]',s8))

# Matching HTML headers
##tags=['<h1>welcome</h1>','<h6>To Apple</h6>','<h3>h7 is value</h3>']
##for tag in tags:
##    print(findall('h[1-6]',tag))
##    
# Matches any number between 0-9
s9='The cost of the book is Rs.100'
##print(findall('[0-9]',s9))

# Matches only lower case letters
s10='hello HOW ARE YOU'
##print(findall('[a-z]',s10))

# Matches only upper case letters
s11='hello HOW ARE YOU'
##print(findall('[A-Z]',s11))

# Matches all upper case and lower case characters
s12='hello HOW ARE YOU'
##print(findall('[A-Za-z]',s12))

# Matches any number between 1-6
# --------------------------------------------------------------------------
# Count total number of Upper case and Lower case letters
# sentence = "Hello World Welcome To Python"
# print(len(findall('[A-Za-z]',sentence)))


# --------------------------------------------------------------------------
# Write a program to count the number of white spaces in a given string
# sentence = "Hello world welcome to Python Hi  How are you. Hi how are you"
# print(len(findall(r'\s',sentence)))
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# matches one or more occurances of "n" between two "a"'s
##s13='annnnnnnnnnna'
##print(findall('an+a',s13))
### matches any digit between 0-9 as long as there is a match
##s14='The cost of the book is Rs.100'
##print(findall('[0-9]+',s14))


# matches lower case alphabets between as long as there is a match
##s15="hello worLD Welcome To Python Programming Pyt123on"
##print(findall('[a-z]+',s15))
# --------------------------------------------------------------------------
# Sum all the numbers in the below string.
# --------------------------------------------------------------------------
##word = "Pytho12nReg567exp2" # 1 + 2 + 5 + 6 + 7 + 2
##print(sum(map(int,findall('[0-9]',word))))

### Adding 12 + 567 + 2
##print(sum(map(int,findall('[0-9]+',word))))

# --------------------------------------------------------------------------
# Meta Character "?" (matches 0 or 1 occurance of previous expression)
# --------------------------------------------------------------------------
##s16="what color do you like we like Blue and Gold colour"
##print(findall('colou?r',s16))
##
##s17='https://www.google.com or http://www.facebook.com'
##print(findall('https?://w+.[a-z]+.[a-z]+',s17))
##
##
###match the jul and july
##s19="Jul the 26th day to July 30th"
##print(findall('July?',s19))


# --------------------------------------------------------------------------
# Negation "^"
# --------------------------------------------------------------------------
# Matches everything apart from numbers between 0-9
##s20='The cost of the book is Rs.100 to 259'
##print(findall('[^0-9]',s20))
##print(findall(r'[A-Za-z\s.]',s20))

# Matches everything apart from alphabets 'a', 'b', 'c' and 'd'


# Matches everything apart from numbers between 0-9
s21='The cost of the book is Rs.100'



# Match only those characters excepts digits
##word = '@hello12world34welcome!123'
##print(findall('[^0-9]',word))

# Count the number of special characters in the below string
sentence = 'hello@world! welcome!!! Python$ hi26 how are you & where are you?'
##print(len(findall(r'[^A-Za-z0-9\s]',sentence)))
# -------------------------------------------------------------------------------------------------
# Starts with "^" and ends with "$"
# -------------------------------------------------------------------------------------------------
##s22='Hello world Hi YasH Hello'
##print(findall('^H[a-z]+',s22))
##print(findall('[A-Za-z]+o$',s22))

##s='hello word hello'
##print(findall('^hello$',s))
##print(findall('^hello$',s))

# string starts with "hello" and ends with "hello" (meaning exactly one word is allowed in the str)
##WB= "what a beautiful day today is"#extact day
##print(findall(r'\bday\b',WB))

##word character : A-Za-z0-9_  , non word character: special character except _ and wide sapce
# -------------------------------------------------------------------------------------------------
# Word Boundary (\b) The expression should be a word boundry 
# (Transition between non-word character to word character or word character to non-word character)
# ------------------------------------------------------------------------------------------------

# ends with word boundry

# starts and ends with word boundry

# Regular expression which matches words that starts with "h"
s23='hello world hi hello universe how are you happy birthday'
##print(findall(r'\bh[a-z]+',s23))

# Regular expression which matches words that starts with "P or J"
s24='Python is a programming language. Python is easier than Java'
##print(findall(r'\b[PJ][a-z]+',s24))

# Regular expression which matches words that ends with "y"
s25='hello world hi hello universe how are you happy birthday feeling very sleepy flying'
##print(findall(r'[a-z]+y\b',s25))

# print only those words starting with vowel character
sentence = "hello hi american english and indian ocean united states"
##print(findall(r'\b[aeiou][a-z]+',sentence))

# Matches only Capital Letter words
s26="This is PYTHON programming LANGUAGE and REGEX"
##print(findall(r'\b[A-Z]+\b',s26))

# Matches only lower case words
s27="This is PYTHON programming LANGUAGE and REGEX"
##print(findall(r'\b[a-z]+\b',s26))

# Matching only pdf files
s28="downloading apple.pdf to downloadspdf folder"
##print(findall(r'\bpdf',s28))

# Different Combintations
line = "03/22 08:51:06 WARNING :.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."
##print(findall(r'\b[A-Za-z]+\b',line))


# ------------------------------------------------------------------------------------------------------------
# Count the number of white spaces in the file
def pattern_count(file_path,pattern):
    with open(file_path) as file:
        Sum=0
        for line in file:
            Sum+=len(findall(pattern,line))
    return (Sum)

# def pattern_count_adv(path,pattern):
#     return sum(len(findall(pattern,line)) for line in open(path))

path=r"C:\Users\Om\Desktop\Python\Advance Python\sample1 (1).txt"
# print(pattern_count(path,r"\s"))

# -------------------------------------------------------------------------------------------------------
# Count the number of Capital Letter words in the file
# print(pattern_count(path,r"\b[A-Z]+\b"))

# -------------------------------------------------------------------------------------------------------
# Count the number of INFO, TRACE, WARNING, EVENT messages in the file
# print(pattern_count(path,r"\bINFO+\b"))
# print(pattern_count(path,r"\bTRACE+\b"))
# print(pattern_count(path,r"\bWARNING+\b"))
# print(pattern_count(path,r"\bEVENT+\b"))


# -------------------------------------------------------------------------------------------------------
# Matches all digits
# print(findall(path,r"\b[0-9]+\b"))
# -------------------------------------------------------------------------------------------------------
sd="654 this string is starting with 12 and ending with numbers 289423784612 890"
##print(findall(r'\d',sd))

# Matches whole numbers
##print(findall(r'\d+',sd))

# Matches sequence of all 3 digit pattern
##print(findall(r'\d{3}',sd))

# Matches exactly 3 digit numbers
##print(findall(r'\b\d{3}\b',sd))

##Matches the starting 3 number.
##print(findall(r'\b^\d{3}\b',sd))
      
##Matches the ending with 3 number.
##print(findall(r'\b\d{3}$\b',sd))

# Matches excatly 6 digit numbers
sd1='Pincode of Bangalore is 560001 and the number is 1234567890'
##print(findall(r'\b\d{6}\b',sd))

# Phone Number pattern (4DIGITS-3DIGITS-3DIGITS)
phone_number=['456-9832-098','9999-8855-89','9164-646-570','88-9875-5236']
##for phno in phone_number:
##    print(findall(r'\d{4}-\d{3}-\d{3}',phno))

# Regular Expression - IP Addresses 3digit.2digit.1digit.1digit
ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']
##for i in ips:
##    print(findall(r'\d{3}.\d{2}.\d{1}.\d{1}',i))

# matching only 800 and 900 numbers
sd="954 this string is starting 999 and ending with numbers 894 9237 84612 890"
##print(findall(r"\b[89]\d{2}\b",sd))

# Extract only 4 digit numbers from the string
sd4="Copyright 1998. All rights reserved"
##print(findall(r'\b\d{4}\b',sd4))

# Regular Expression - PAN Number
##sentence = "my pan number is ABCDE1234X and the other number is XYZTR3104J id is 123XYZTR3104J89"
##print(findall(r"\b[A-Z]{5}\d{4}[A-Z]\b",sentence))

# Regular expression for matching only 3 letter words in the given string
##sentence = "hello hi how are you what is your name he is older than me how old are you"
##print(findall(r"\b[a-z]{3}\b",sentence))

# o/p ['how', 'are', 'you', 'how', 'old', 'are', 'you']

# --------------------------------------------------------------------------
# Meta Character "*" (matches 0 or more occurances of previous expression)
# --------------------------------------------------------------------------

# Regular expression for matching the words which starts with "he"
sentence = "he helps the community and he is the hero of the day"
##print(findall(r"\bhe[a-z]*",sentence))

# -------------------------------------------------------------------------------------------------------
# Groups ( | )
# -------------------------------------------------------------------------------------------------------------
# Matches either "python" or "java"
##py='python and java are object oriented'
##print(findall(r"(python|java)",py))

# Regular Expression for Matching Inbox, Inbox(1), .... Inbox(N)

# Regular expression for matching the words which either starts with "he" or "se"
sentence = "he helps the community and he is the hero of the day she sells sea shells on the sea shore"
##print(findall(r"(\bhe[a-z]*|\bse[a-z]*)",sentence))
##print(findall(r"\b(he|se)[a-z]*",sentence))

# Match only those lines that were logged in year 98
years=("data logged in 1999",
       "data logged in 1998",
       "data logged in 2000",
       "data logged in 1997",
       "data logged in 1898",
       "data logged in 2026")
##for year in years:
##    if findall(r'\d{2}98',year):
##        print(year)
       
       
# Regular Expression - YYYY-MM-DD date format
dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']
##for date in dates:
##    if findall(r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[01])",date):
##        print(date)
##(?:0[1-9]|1[0-9]|2[0-9]|3[01]) optimized 0[1-9]|[12]\d|3[01]
        
# Regular Expression - 24hr time format
formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']


# Regular Expression - 24hr time format
_formats = ['00:00:00', '23:59:59', '24:00:00', '1:59:20', '12:9:10', '10:20:8']
# ------------------------------------------------------------------------------------------------------------
# \ escaping meta characters
# ------------------------------------------------------------------------------------------------------------
# Count the number of occurances of question marks ("?") in the below string
line = "hello there.. how are you? how is it going?? what are you doing? ... "
##print(len(findall(r'\?',line)))

# Count the number of occurances of dots(".") in the below string
line = "hello there..... how are you? how is it going?? what are you doing? ... "
##print(len(findall(r'\.',line)))

# Count the number of occurances of stars ("*") in the below string
line = "hello there..... how are you? *** how is it going?? what * are you  ** doing? ... "
#---------------------------------------------------------------------------------------
# Replacing patterns
# ------------------------------------------------------------------------------------------------------
# Replace all vowels with "*"
sentence = "hello world welcome to python"
##print(sub("[aeiou]",'*',sentence))

# Replace all occurances of digits with "*"
sd="654 this string is starting with 12 and ending with numbers 289423784612 890"
print(sub("\d","*",sd))

# Replace all occurances of special characters with " "
sentence = 'hello#$%world welcome@!#$%to python*&^%'
print(sub("[^A-Za-z0-9\s]"," ",sentence))

#Replace "And" with "&"
sentence = "Java and Python are programming languages"
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# Replace whitespaces with newline character in the below string
sentence = "Hello world welcome to python"
# ------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# dot "." matches with everything
# ------------------------------------------------------------------------------------------------------
