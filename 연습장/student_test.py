class Student:
    def __init__(self, name, kor, mat, eng, sci):
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng
        self.sci = sci

    def get_sum(self):
        return self.kor + self.mat + self.eng + self.sci
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("운인성", 87,98,88,95),
    Student("연하진", 44,56,90,25),
    Student("구지연", 60,50,40,20),
    Student("나선주", 55,60,54,12),
    Student("윤아린", 47,58,45,32),
    Student("윤명월", 45,56,58,12),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

student_a = Student("윤인성", 87,98,88,95),
student_b = Student("연하진", 92,98,96,98),

print(student_a == student_b)
print(student_a != student_b)
print(student_a > student_b)
print(student_a >= student_b)
print(student_a < student_b)
print(student_a <= student_b)
