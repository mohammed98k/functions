import random

print(f"""Name: Mohammed Abuhashem
Submission Date: 31 / 08 / 2023""")

course_name = input("course name: ")
class Course:
    def __init__(self, course_name, course_mark):

        self.course_id = random.randint(10000, 99999)
        self.course_name = course_name
        self.course_mark = course_mark



class Student:
    count = 0


    def __init__(self, student_name, student_age , student_number):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.count += 1


    def enroll_course(self, course_name, course_mark):
        new_course = Course(course_name, course_mark)
        self.courses_list.append(new_course)
        print(f"Course '{course_name}' enrolled successfully with mark {course_mark}")

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_mark = 0
        for course in self.courses_list:
            total_mark += course.course_mark
            return ("average: ", total_mark / len(self.courses_list))

student_list = []

while True:
    try:

        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except:
        print("invalid input")
        #continue


    if selection == 1:
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")


        new_student = (student_number,student_name,student_age)
        student_list.append(new_student)
        print("Student Added Successfully")
    elif selection == 2:
        student_number = int(input("Enter Student Number"))
        for student in student_list:
            if student == student_number:
                student_list.remove(student)
        else:
            print("Student Not Exist")
    elif selection == 3:
        student_number = int(input("Enter Student Number"))
        for student in student_list:
            if student == student_number:
                print(f"""{student_name}, {student_age}""")
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        for student in student_list:
            if student == student_number:
                average = student.get_student_average()
                print(f"Student Average: {average}")
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        for student in student_list:
            if student == student_number:
                course_name = input("add course name: ")
                course_mark = int(input("add course mark: "))
                new_course = Course(course_name , course_mark)
                student.__init__(new_course)
            else:
                print("Student Not Exist")

    elif selection == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please select a valid option.")



