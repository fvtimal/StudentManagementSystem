from User import User
from Student import Student

class Admin(User):

    students = []

    def __init__(self,id,name,email,role):

        super().__init__(id,name,email)
        self.__role = role

        if not Admin.students:
            Admin.students = Admin.load_students()

    def addStudent(self,name,email,program,gpa,sem):
        std = Student(name,email,program,gpa,sem)
        Admin.students.append(std)




    


    @classmethod
    def load_students(cls):

        students = []

        try:
            file = open("students.txt","r")

            for line in file:
                std = Student.from_string(line.strip())
                students.append(std)

            file.close()

        except FileNotFoundError:
            print("no file found")


        return students




