class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Hello, I am {self.name}, {self.gender} and {self.age} years young')
test1 = Person('Spock', 25, 'male')
test1.introduce()