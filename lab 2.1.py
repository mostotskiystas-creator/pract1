# Батьківський клас
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Мене звати {self.name}, мені {self.age} років")

    def work(self):
        print("Людина працює")


# Дочірній клас
class Student(Human):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university   # інкапсуляція (приватне поле)

    # getter
    def get_university(self):
        return self.__university

    # setter
    def set_university(self, university):
        self.__university = university

    # поліморфізм (перевизначення методу)
    def work(self):
        print("Студент навчається")


# Використання
person = Human("Олег", 40)
person.introduce()
person.work()

student = Student("Ірина", 20, "ЛНУ")
student.introduce()
student.work()
print("Університет:", student.get_university())
