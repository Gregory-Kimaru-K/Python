class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} : {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    

student1 = Student("Sandy", 4.0)
student2 = Student("Spongebob", 3.2)
student3 = Student("Squidward", 2.9)
student4 = Student("Mr. Krabs", 2.5)

students = [student1, student2, student3, student4]
for student in students:
    print(student.get_info())

print(Student.get_count())
print(Student.get_average_gpa())