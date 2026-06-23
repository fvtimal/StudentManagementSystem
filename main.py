from Admin import Admin


admin = Admin("46546","aila","fg@gmail.com","coodinator")


while True:

    print("Student Management System")
    print("1. add student")
    print("2. delete student")
    print("3. display students")
    print("4. exit")


    choice = input("enter choice: ")


    if choice == "1":

        id = input("User ID:")
        name = input("Student name: ")
        email = input("Student email: ")
        program = input("Program: ")
        gpa = float(input("GPA: "))
        sem = input("Semester: ")

        admin.addStudent(
            id,
            name,
            email,
            program,
            gpa,
            sem
        )


    elif choice == "2":

        roll = input("Enter roll number: ")

        admin.deleteStudent(roll)


    elif choice == "3":

        for student in Admin.students:
            student.displayProfile()
            print("\n")


    elif choice == "4":

        print("Exiting...")
        break


    else:
        print("Invalid choice")