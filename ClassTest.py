
class UT_Student:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def intro_name(self):
        print('My name is ', self.name, '.')

    def intro_age(self):
        print('I am ', self.age, ' years old.')

    def intro_hobby(self):
        print('I like ', self.hobby, '.')

    def self_intro(self):
        self.intro_name()
        self.intro_age()
        self.intro_hobby()

if __name__ == '__main__':
    UT_Student('Matt','30','fishing').intro_age()