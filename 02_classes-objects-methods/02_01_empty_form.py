# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class Form:

    def __init__(self, name, age, gender, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        
    
    def name(self, name):
        print(f'your name is {name}')
        self.name = name

    def __str__(self):
        return f'{self.name} {self.age} {self.gender} {self.nationality}'
    
    def __repr__(self) -> str:
        return f'Form(name={self.name}, age={self.age}, gender={self.gender},  nationality={self.nationality})'


i = Form('Narayan',30,'Male','Danish')

print(i)
        