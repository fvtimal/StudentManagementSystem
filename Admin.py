from User import User

class Admin(User):

    def __init__(self,id,name,email,role):

        super().__init__(id,name,email)
        self.__role = role


