# Write a program that print the total number of students those have less than 2.5 GPA in
# AI? (with and without using for loop)

studentData = {'2018-CS-1': [('DSA', 3), ('Algo', 2.5), ('AI', 3)],
               '2018-CS-2': [('LA', 2.7), ('AI', 2.3), ('PF', 3.2)],
               '2018-CS-3': [('OOP', 3), ('DSA', 3.5), ('PF', 3)],}

def students_less_gpa_with_forloop():              
    count = 0
    for std in studentData:
        for subject in studentData[std]:
            if (subject[0] == 'AI' and subject[1] < 2.5):
                count += 1

    print('The total number of students those have less than 2.5 GPA in AI: ', count)

def students_less_gpa_without_forloop():
    stdcount = 0
    students = list(studentData.keys())
    count = len(students)
    while count > 0:
        student = students[count - 1]
        subjects = studentData[student]
        subject_count = len(subjects)
        while subject_count > 0:
            if subjects[subject_count - 1][0] == 'AI' and subjects[subject_count - 1][1] < 2.5:
                stdcount += 1
            subject_count -= 1
        count -= 1
    print('The total number of students those have less than 2.5 GPA in AI: ', stdcount)

students_less_gpa_with_forloop()
students_less_gpa_without_forloop()