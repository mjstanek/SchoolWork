#1 create variables for name, fave color and age, then print them
# name = 'Matt'
# color = 'Red'
# age = 30

# regular printing
# print('My name is ', name, '. My favorite color is ', color, '. I am ', age, 'years old.')
# f-string
# print(f'My name is {name}. My favorite color is {color} and I am {age} years old.')

#2 create string variable for book title, integer variable for number of pages and float for amazon rating
#gather user input and print them
#
# title = str(input('Please type the name of a book. '))
# pages = int(input("Please type the number of pages in this book. "))
# rating = float(input("Please type the current Amazon score rating for this book. "))
#
# print(f'The book {title} is {pages} pages long and has an Amazon rating of {rating} stars.')

#3 create a list of three favorite foods, add one using append and remove one using remove
#
# foods = ['pizza', 'cheeseburger', 'french fries']
# print(foods)
# foods.append('milkshake')
# print(foods)
# foods.remove('french fries')
# print(foods)

#4 create dictionary of car information and print it
#
# car = {
#     'make' : 'Ford',
#     'model' : 'F150',
#     'year' : 2016,
#     'color' : 'silver'
# }
#
# print(f'My car is a {car.get("color")} {car.get("make")} {car.get("model")} from {car.get("year")}.')

#5 ask user for a number and return if the number is odd or even

# def oddoreven():
#     number = int(input("Please enter a whole number and I will tell you whether it is odd or even. "))
#     if number %2 == 0:
#         print(f'The number {number} is even.')
#     else:
#         print(f'The number {number} is odd.')
#
# oddoreven()

#6 use a while loop to count down from 10 to 1 and say blast off
#
# def countdown():
#     start = 10
#     while start > 0:
#         print(start)
#         start = start-1
#     else:
#         print('Blast off!')
#
# countdown()

#7 ask for number and print it's square, use try except to tell user they must enter a number
#
# def square():
#     number = input('Please enter a number and I will return its square. ')
#     try:
#         square = int(number)**2
#         print(square)
#     except ValueError:
#         print('Sorry, you must enter a number. Please try again.')
#
# square()

#8 create function to greet a list of names individually
#
# names = ['Matt', 'Tori', 'Lois']
#
# def greeting():
#     for name in names:
#         print(f'Hello {name}! Welcome to Tampa!')
#
# greeting()

#9 iterate through a list of 5 numbers and list that number's square

# numbers = [456, 65, 985412, 1845, 6985]
#
# def square():
#     for number in numbers:
#         square = number**2
#         print(f'The square of {number} is {square}.')
#
# square()

#10 given a list of miles, create a new list of kilometers equal to miles
#
# miles = [1, 5, 10, 36, 120]
# print(miles)
#
# def conversion():
#     kilometers = []
#     for distance in miles:
#         km = distance * 1.61
#         kilometers.append(km)
#
#     print(kilometers)
#
# conversion()

#11 iterate through dictionary to print book and author
#
# books_and_authors = {
#     "To Kill a Mockingbird": "Harper Lee",
#     "1984": "George Orwell",
#     "The Great Gatsby": "F. Scott Fitzgerald",
#     "Moby Dick": "Herman Melville",
#     "War and Peace": "Leo Tolstoy",
#     "The Catcher in the Rye": "J.D. Salinger"
# }
#
# titles = []
# for x in books_and_authors.keys():
#     titles.append(x)
#
# y=0
# for entry in titles:
#     title = titles[y]
#     y = y+1
#     author = books_and_authors.get(title)
#     print(f'The book "{title}" was written by {author}.')

#12 use a for loop to loop through a list of integers and insert even integers into their own list
#
# integers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# listofevens = []
#
# for x in integers_list:
#     try:
#         if x%2 == 0:
#             listofevens.append(x)
#     except ValueError:
#         y=0
#
# print(listofevens)

#13 given a list of names, concatenate them with "is a friend of"
#
# listofnames = ['paul', 'lucy', 'bob', 'lily']
# phrase = ' is a friend of '
# print(phrase.join(listofnames))

