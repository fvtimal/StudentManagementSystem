from User import User

class Student(User):

    roll = 1

    def __init__(self,id,name,email,program,gpa,sem):

        super().__init__(id,name,email)

        rollNo = "ST" + str(Student.roll)
        Student.roll += 1

        self.__rollNo = rollNo
        self.__program = program
        self.__gpa = gpa
        self.__sem = sem
        self.__status = self.statusCheck()

    def getRollNo(self):
        return self.__rollNo

    def getProgram(self):
        return self.__program

    def getGPA(self):
        return self.__gpa

    def getSem(self):
        return self.__sem

    def statusCheck(self):
        if self.__gpa >= 3.5:
            return "Excellent"
        elif self.__gpa >= 2.5:
            return "Good"
        else:
            return "Warning"

    def toString(self):
        return (f"{self.__rollNo},{self.getID()},{self.getName()},{self.getEmail()}," 
                f"{self.__program},{self.__gpa},{self.__sem},"
                f"{self.__status}\n")

    def displayProfile(self):
        print("Student ID:", self.__rollNo)
        print(self.getName(), "|", self.getEmail())
        print("program: " + self.__program)
        print("semester: " + str(self.__sem))
        print("gpa: " + str(self.__gpa))
        print("status:" + self.statusCheck())

    @classmethod
    def from_string(cls,line):
        parts = line.split(",")

        rollNo = parts[0]
        id     = parts[1]
        name   = parts[2]
        email  = parts[3]
        program= parts[4]
        gpa    = float(parts[5])
        sem    = parts[6]
        obj = cls.__new__(cls)
        User.__init__(obj,id,name,email)
        obj._Student__rollNo  = rollNo
        obj._Student__program = program
        obj._Student__gpa     = gpa
        obj._Student__sem     = sem
        obj._Student__status  = obj.statusCheck()
        print("hello")
        return obj