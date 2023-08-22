with open("details.txt","w") as file:
    students = []
    name = input("student name: ")
    age = int(input("student age: "))
    dob = int(input("student dob: "))
    informations = {"name": name , "age" : age , "dob" : dob}
    file.write(f"Name: {name}\nAge: {age}\nDOB: {dob}\n")
    students.append(informations)
    file.close()
    print(students)
