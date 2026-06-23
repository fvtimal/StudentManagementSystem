from User import User
from Student import Student

class Admin(User):

    students = []

    def __init__(self,id,name,email,role):

        super().__init__(id,name,email)
        self.__role = role

        if not Admin.students:
            Admin.students = Admin.load_students()


    def addStudent(self,id,name,email,program,gpa,sem):
        std = Student(id,name,email,program,gpa,sem)
        Admin.students.append(std)
        Admin.save_students()

        print("student successfully added")

    def deleteStudent(self,rollNo):

        for std in Admin.students:
            if std.getRollNo() == rollNo:
                Admin.students.remove(std)
                Admin.save_students()
                print("Student deleted")
                return

        print("student not found")

    def searchByProgram(self, program):
        return [std for std in Admin.students if std.getProgram().lower() == program.lower()]

    def displaySortedByGPA(self):
        sorted_students = sorted(Admin.students, key=lambda s: s.getGPA(), reverse=True)
        for std in sorted_students:
            std.displayProfile()
            print("---")


    @classmethod
    def load_students(cls):

        students = []

        try:
            file = open("../data/students.txt", "r")

            for line in file:
                std = Student.from_string(line.strip())
                students.append(std)

            file.close()

            if students:
                last = int(students[-1].getRollNo().replace("ST", ""))
                Student.roll = last + 1

        except FileNotFoundError:
            print("no file found")

        return students


    @classmethod
    def save_students(cls):

        file = open("../data/students.txt", "w")

        for std in Admin.students:
            file.write(std.toString())

        file.close()


    def revert_test(self):
        print("file two")



