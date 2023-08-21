with open("details.txt","w") as file:
    students = []
    name = input("student name: ")
    age = int(input("student age: "))
    dob = int(input("student dob: "))
    informations = {"name": name , "age" : age , "dob" : dob}
    students.append(informations)
    file.close()
    print(students)