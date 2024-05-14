from math import *
print("Hello")

# printing shapes
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /____|")

# variables and data types
character_subject = "CS"
print("I love " + character_subject + " !!")

#strings
phrase = "This is a test"
print(phrase.upper())
print(phrase.islower())
print(len(phrase))
print(phrase[2])

#numbers
print(3 * (4 + 5))
print(10 % 3)

my_num= 5
print(str(my_num) + " is my favorite number!")
print(pow(3, 3))
print(sqrt(36))

#input from users
name = input("Please enter your name: ")
print("Hello " + name + "!")


#basic calculator
num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")
result = float(num1) + float(num2)
print(result)

#madlibs
color = input("Enter any color: ")
plural_noun = input("Enter any plural noun: ")
celebrity = input("Enter any celebrity name: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

#lists
friends = ["Jacob", "Hannah", "Jake", "Barbara"]
print(friends[0])
friends[0] = "Alice"
print(friends[0:2])

#lists functions
lucky_numbers = [4, 11, 24, 16, 1]
fruits = ["Apple", "Orange", "Banana", "Kiwi", "Strawberry"]

# extend function for list: take one list and append it to the end of other list
fruits.extend(lucky_numbers)
print(fruits)

#add individual elements to the end of list using append function
fruits.append("Blueberries")

#add individual elements to anywhere in the list using insert function
fruits.insert(1, "blackberries")

#remove elements
fruits.remove("blackberries")

#remove element from the end of the list
fruits.pop()

#clear/remove the entire list
fruits.clear()

#look up if an element is present in the list
print(fruits.index("apple"))

#can get the count of elements in the list
print(fruits.count("orange"))

#sort the list
fruits.sort()

#copy a list
fruits2 = fruits.copy()

#TUPLES: TUPLE is immutable
coordinates = (4, 5)
print(coordinates[1])

#functions
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))
    
say_hi("Hannah", 24)

#return statements
def cube(num):
    return num*num*num

result = cube(3)
print(result)

#if statements
is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are neither a male nor tall.")
    
#if statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >=num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))

#advanced calculator
num1 = float(input("Please enter a number: "))
op = input("Please an operator: ")
num2 = float(input("Please enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/": 
    print(num1 / num2)
else:
    print("Invalid operator")

#dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Nov"])
print(monthConversions("Luv", "Not a valid value"))