#1 list filtering
#Given a list of words ["apple", "banana","cherry","date"]
# write a loop to print only the words that contains the letter ‘a’.,
import random

# string = 'apple'
# if 'a' in string:
#     print('There is an A')

# listoffruits = ["Apple", "banana","cherry","date"]
#
# for fruit in listoffruits:
#     if 'a' in fruit.lower():
#         print(fruit)

#2 String Character Count
#Write a python program to count the number of
# occurenece of letter “a” in the string “banana”.

# y = 0
#
# for x in 'banana':
#     if x.lower() == 'a':
#         y = y + 1
#
# print(f'The letter A is in the word banana {y} times.')

#3 List Append and Comprehension
#Given a list of distances in miles, use list comprehension
# or append() to create a new list with the distances
# converted to kilometer. ( 1 miles = 1.61 km)
#
# miles = [1, 2, 6, 9, 81]
# kilometers = []
#
# for x in miles:
#     km = x * 1.61
#     kilometers.append(km)
#
# print(miles)
# print(kilometers)

#ALTERNATIVELY

# kilometers = [km*1.61 for km in miles]
# print(kilometers)

#4 String Reversal
#write a program to reverse the string "hello Tampa" using a loop
#save the reversed characters in a list
#
# message = "Hello Tampa"
# reversedmessage = ""
# reversedmessage2 = ""
# reversedlist = []
#

#ALTERNATIVELY
# message = message[::-1]
# print(message)

# for z in message:
#     reversedmessage2 = z + reversedmessage2
#
# print(reversedmessage2)
#
# for x in message:
#     reversedlist.insert(0, x)
#
# print(reversedlist)
#
# for y in reversedlist:
#     reversedmessage = reversedmessage + y
#
# print(reversedmessage)

#5 Arithmetic calculation
#Given the following lengths [1,2,3,4,5,6,7,8,9,10] for a square like
#shape, calculate the area for even-numbered lengths
#
# lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for x in lengths:
#     if x%2 == 0:
#         area = x*x
#         print(f'The area of the square with a length of {x} is {area}.')

#6 Math Quiz Game
# Generate a simple math quiz with random addition questions.
# Track the number of correct answers and provide final score.
# Need to create two variables to contains two random numbers
# Need to create a counters track number of questions being generated
# Need to create an if loop to check the if the answer is correct

# one = random.randrange(0,100)
# two = random.randrange(0,100)
# operation = random.randrange(0,3)
#
# question = f''

#CLASS CONVERSION 1

#ORIGINAL
# def add(x, y):
#     return x + y
#
# # Function to subtract two numbers
# def subtract(x, y):
#     return x - y
#
# # Function to multiply two numbers
# def multiply(x, y):
#     return x * y
#
# # Function to divide two numbers
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y
#

# class Calculator:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def add(self):
#         return self.x + self.y
#
#     # Function to subtract two numbers
#     def subtract(self):
#         return self.x - self.y
#
#     # Function to multiply two numbers
#     def multiply(self):
#         return self.x * self.y
#
#     # Function to divide two numbers
#     def divide(self):
#         if self.y == 0:
#             return "Error! Division by zero."
#         else:
#             return self.x / self.y
#
# print(Calculator(4,2).add())

#CLASS CONVERSION 2

#ORIGINAL

# accounts = {
#     1001: {'name': 'Alice', 'balance': 1000},
#     1002: {'name': 'Bob', 'balance': 1500},
# }
#
# # Function to create a new account
# def create_account(account_number, name, initial_deposit):
#     if account_number in accounts:
#         print("Account number already exists.")
#     else:
#         accounts[account_number] = {'name': name, 'balance': initial_deposit}
#         print(f"Account created for {name}. Account Number: {account_number}, Initial Deposit: {initial_deposit}")
#
# # Function to deposit money into an account
# def deposit(account_number, amount):
#     if account_number in accounts:
#         accounts[account_number]['balance'] += amount
#         print(f"Deposited {amount}. New balance is {accounts[account_number]['balance']}.")
#     else:
#         print("Account number does not exist.")
#
# # Function to withdraw money from an account
# def withdraw(account_number, amount):
#     if account_number in accounts:
#         if accounts[account_number]['balance'] >= amount:
#             accounts[account_number]['balance'] -= amount
#             print(f"Withdrew {amount}. Remaining balance is {accounts[account_number]['balance']}.")
#         else:
#             print("Insufficient funds.")
#     else:
#         print("Account number does not exist.")
#
# # Function to check the balance of an account
# def check_balance(account_number):
#     if account_number in accounts:
#         print(f"Account balance for account {account_number}: {accounts[account_number]['balance']}")
#     else:
#         print("Account number does not exist.")

#Conversion

class Bank:
    def __init__(self):
        self.accounts = {
            1001: {'name': 'Alice', 'balance': 1000},
            1002: {'name': 'Bob', 'balance': 1500},
        }

    # Function to create a new account
    def create_account(self, account_number, name, initial_deposit):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = {'name': name, 'balance': initial_deposit}
            print(f"Account created for {name}. Account Number: {account_number}, Initial Deposit: {initial_deposit}")

    # Function to deposit money into an account
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount}. New balance is {self.accounts[account_number]['balance']}.")
        else:
            print("Account number does not exist.")

    # Function to withdraw money from an account
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew {amount}. Remaining balance is {self.accounts[account_number]['balance']}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Function to check the balance of an account
    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account balance for account {account_number}: {self.accounts[account_number]['balance']}")
        else:
            print("Account number does not exist.")

variable = Bank()
variable.create_account(1003, 'PC', 1000000)
variable.withdraw(1003, 100000)
