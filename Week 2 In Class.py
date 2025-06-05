# student_name = "Matt Stanek"
# student_hobby = 'working out'
# student_age = 30
# print(student_name, student_hobby, student_age)

# student_names = ['Matt Stanek', 'John Doe', 'Jim Smith']
# # student_age = [16, 17, 18, 19]
# print(student_names[1:])
# for x,y  in zip(student_names,student_age):
#     # print(x, 'is', y, 'years old')
#     print (f'{x} is {y} years old')

student_profile = {'matt':[30, 'weightlifting', 6.2, 300], 'tom': [46, 'football', 6.4, 210], 'steven':[33, 'hockey', 5.9, 195]}
print(student_profile['tom'][1])
# welcome to Tampa, Matt! He is 30 years old and likes weightlifting.
# for x in student_profile:
    # print(f'Welcome to Tampa, {x}! He is {student_profile[x][0]} years old and likes {student_profile[x][1]}.')
    # bmicalculator(student_profile[x][2], student_profile[x][3])
# for x in student_profile:
#     print(student_profile[x])

def bmicalculator(height, weight):
    inches = height*12
    inches2 = inches*inches
    bmi=(weight/inches2)*703
    if bmi < 18.5:
        print("Your bmi is ", bmi, "you are underweight")
    elif   bmi> 30:
        print("Your bmi is ", bmi, "you are overweight")
    else:
        print("Your bmi is ", bmi, "you are at a good weight")

for x in student_profile:
    print(f'Welcome to Tampa, {x}! He is {student_profile[x][0]} years old and likes {student_profile[x][1]}.')
    bmicalculator(student_profile[x][2], student_profile[x][3])