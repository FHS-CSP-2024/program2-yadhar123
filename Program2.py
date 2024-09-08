# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.


name = input("what is your name?")
print (name)
print (name)


## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input ("what is your name?")
print("!" + name + "!" + name + "!")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

firstname = input("what is your name?")
lastname = input("what is your first name?")
streetaddress = input("what is your street adress")
postcode = input("what is your city and postal code?")
print ("Here is all your info together :)")
print (firstname)
print (lastname)
print (streetaddress)
print (postcode)


## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out

word1= input("Enter word 1")
word2= input("Enter word 2")
word3= input("Enter word 3")

print (word1 + "_" +word2+"_" + word3)

## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses thQQQQat information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

name= input("enter a anme for your very own fictional character:")
year = input("what year do you want him/her to be in? ENter a future year here: ")
print (name +"is a very magical person, born in the year" +year +".")
print("In a world filled with rainbows and unicorns " + name + "was known for their magical powers")
print("one day in the year"+ year+ "," +name+ "discovered a shrek that could run and only one person knew how to solve it, it was" +name+"Knew how to find whats right.")