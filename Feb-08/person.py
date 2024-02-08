# инкапсуляция
# геттер и сеттер

class Gender:
    male = 'male'
    female = 'female'
    non_binary = 'non_binary'

class Person:
    __first_name: str
    __last_name: str
    __gender: str
    __age: int
    __partner = None

    def __init__(self, gender, full_name, age):
        self.__gender = gender
        self.__age = age
        self.__first_name, self.__last_name = full_name.split()
        
    @property

    def name(self):
        return f"{self.__first_name} {self.__last_name}"







        
    def info(self):
        msg =  f"Person: {self.__first_name} {self.__last_name} {self.__gender} {self.__age} лет"
        if self.__partner:
            msg += f",в браке с {self.__partner.__first_name} {self.__partner.__last_name}"
        return msg

    def __str__(self):
        return self.info()
        
    def __repr__(self):
        return self.info()
    
    def __add__(self, other):
        return self.marry(other)
    def marry(self, other):
        if self.__partner or other.__partner:
            return
        if self is other:
            return
        if self.__age < 18 or other.__age < 18:
            return
        if self.__gender == other.__gender:
            return
        self.__partner, other.partner = other, self
        if self.__gender == Gender.female:
            self.__last_name = other.__last_name
        elif other.gender == Gender.female:
            other.last_name = self.__last_name
        print(f"Поздравляем со свадьбой, {self.__first_name} {self.__last_name}, и {other.__first_name} {other.__last_name}")
        

natalie = Person(Gender.female, 'Natalie Portman', 42)
temirlan = Person(Gender.male, 'Temirlan Ibrayev', 18)
ayan = Person(Gender.male, 'Ayan Urazaliev', 10)
alan = Person(Gender.non_binary, 'Alan Xz', 21)
alana = Person(Gender.female, 'Alana Alana', 27)
pamela = Person(Gender.female, 'Pamela Andersen', 42)

natalie.marry(alan)
temirlan.marry(natalie)
ayan.marry(alana)

print(natalie.info())
print(temirlan.info())
print(alan.info())
print(alana.info())
print(ayan.info())
print(pamela.info())

natalie.__last_name = "Urazaliyeva"
natalie.__partner = ayan
print()
# print(natalie.info())
# print(temirlan.info())
# print(ayan.info())


print(str(temirlan))
print(natalie.name)