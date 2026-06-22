from User import User

class Student(User):

    roll = 1

    def __init__(self,name,email,program,gpa,sem):

        super().__init__(id,name,email)

        rollNo = "ST" + str(Student.roll)
        Student.roll += 1

        self.__rollNo = rollNo
        self.__program = program
        self.__marks = gpa
        self.__sem = sem




