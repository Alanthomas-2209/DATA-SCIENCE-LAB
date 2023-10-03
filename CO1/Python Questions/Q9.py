# 9.	Given a file “mark.csv” of student data with the fields rollno, name, branch, m1, m2, m3,  write python code to
# •	Print total marks of all students
# •	Find the average mark of each subject
# •	Find the student with highest and second highest mark.


import csv

total_marks = 0
subject_sums = {'m1': 0, 'm2': 0, 'm3': 0}
highest_mark = -1
second_highest_mark = -1
highest_mark_student = ''
second_highest_mark_student = ''

with open('CO1\Python Questions\mark.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        rollno = row['rollno']
        name = row['name']
        m1 = int(row['m1'])
        m2 = int(row['m2'])
        m3 = int(row['m3'])
        total_student_marks = m1 + m2 + m3
        total_marks += total_student_marks
        
        subject_sums['m1'] += m1
        subject_sums['m2'] += m2
        subject_sums['m3'] += m3
        
        if total_student_marks > highest_mark:
            second_highest_mark = highest_mark
            second_highest_mark_student = highest_mark_student
            highest_mark = total_student_marks
            highest_mark_student = f"{rollno} - {name}"
        elif total_student_marks > second_highest_mark:
            second_highest_mark = total_student_marks
            second_highest_mark_student = f"{rollno} - {name}"

num_students = csv_reader.line_num - 1  
average_marks = {subject: subject_sums[subject] / num_students for subject in subject_sums}

print(f"Total Marks of All Students: {total_marks}")
print("Average Marks for Each Subject:")
for subject, avg in average_marks.items():
    print(f"{subject}: {avg:.2f}")
print(f"Highest Mark Student: {highest_mark_student} (Total Marks: {highest_mark})")
print(f"Second Highest Mark Student: {second_highest_mark_student} (Total Marks: {second_highest_mark})")
