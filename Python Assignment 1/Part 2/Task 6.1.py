# Write a program which shall print GPA of all students. Assume all subject have 3 credit
# hours. (with and without using for loop)

studentData = {'2018-CS-1': [('DSA', 3), ('Algo', 2.5), ('AI', 3)],
               '2018-CS-2': [('LA', 2.7), ('AI', 2.3), ('PF', 3.2)],
               '2018-CS-3': [('OOP', 3), ('DSA', 3.5), ('PF', 3)], }


def gpa_with_for_loop():
    for std in studentData:
        gpa = 0
        for subject in studentData[std]:
            gpa += subject[1] * 3
        gpa = gpa / (len(studentData[std]) * 3)
        print("Name: ", std, " | GPA: ", gpa)


def gpa_without_for_loop():
    students = list(studentData.keys())
    print(students)
    count = len(students)
    while count > 0:
        gpa = 0
        student = students[count - 1]
        subjects = studentData[student]
        subject_count = len(subjects)
        while subject_count > 0:
            gpa += subjects[subject_count - 1][1] * 3
            subject_count -= 1
        gpa = gpa / (len(subjects) * 3)
        print("Name: ", students[count - 1], " | GPA: ", gpa)
        count -= 1


gpa_with_for_loop()
gpa_without_for_loop()
