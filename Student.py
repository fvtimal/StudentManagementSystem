from User import User

class Student(User):

    roll = 1

    def __init__(self,name,email,program,gpa,sem):

        super().__init__(id,name,email)

        rollNo = "ST" + str(Student.roll)
        Student.roll += 1

        self.__rollNo = rollNo
        self.__program = program
        self.__gpa = gpa
        self.__sem = sem
        self.__status

    def statusCheck(self):
        if self.__gpa >= 3.5:
            return "Excellent"
        elif self.__gpa >= 2.5:
            return "Good"
        else:
            return "Warning"

    def toString(self):
        return (f"{self.__rollNo},{self.name},{self.email},"
                f"{self.__program},{self.__gpa},{self.__sem},"
                f"{self.__status}\n")


    def displayProfile(self):
        print("Student ID:", self.__rollNo)
        print(super.getName(), "|", super.getEmail())
        print("program: " + self.__program)
        print("semester: " + self.__sem)
        print("gpa: " + self.__gpa)
        print("status:" + self.statusCheck())






