students_num = int(input("the number of students"))
marks_num = int(input("the number of marks"))
student_marks = []
for i in range(0, students_num):
    for i in range (0,marks_num):
        my_mark = float(input(f"student mark {i+1}"))
        student_marks.append(my_mark)
    average = sum(student_marks) / len(student_marks)

    print("average: ",average)
    print("max_student_marks: ",max(student_marks))
    print("min_student_marks: ",min(student_marks))