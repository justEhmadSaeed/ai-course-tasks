# Write a program that print the highest number obtained in DSA (with and without using
# for loop)

studentData = {'2018-CS-1': [('DSA', 3), ('Algo', 2.5), ('AI', 3)],
               '2018-CS-2': [('LA', 2.7), ('AI', 2.3), ('PF', 3.2)],
               '2018-CS-3': [('OOP', 3), ('DSA', 3.5), ('PF', 3)],}
def highest_number_with_forloop():
    max = 0
    for std in studentData:
        for subject in studentData[std]:
            if (subject[0] == 'DSA' and subject[1] > max):
                max = subject[1]
                
    print('Highest Marks in DSA: ', max)


def highest_number_without_forloop():
    max = 0
    students = list(studentData.keys())
    count = len(students)
    while count > 0:
        student = students[count - 1]
        subjects = studentData[student]
        subject_count = len(subjects)
        while subject_count > 0:
            if subjects[subject_count - 1][0] == 'DSA' and subjects[subject_count - 1][1] > max:
                max = subjects[subject_count - 1][1]
            subject_count -= 1
        count -= 1
    
    print('Highest Marks in DSA: ', max)

highest_number_with_forloop()
highest_number_without_forloop()