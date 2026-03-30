class Person:  # class name always Capital letter hobe
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # super diye parent class er init ke call kora hoise
        self.subject = subject
        self.__grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.__grades.append(score)

    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"{self.name} | {self.subject} | avg: {self.average(): .1f}"
