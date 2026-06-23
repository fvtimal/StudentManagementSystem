class User:
    def __init__(self,id,name,email):
        self.__id = id
        self.__name = name
        self.__email = email

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setName(self,name):
        self.__name = name

    def setEmail(self,email):
        self.__email = email


    def displayProfile(self):
        print("ID: " + self.__id)
        print("Name: " + self.__name)
        print("Email: " + self.__email)

    def updateProfile(self,name,email):
        self.setName(name)
        self.setEmail(email)
        self.displayProfile()

    
