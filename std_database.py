#initializing the program and creating the function

def manage_student_database():
    students = []
    student_id = 1

    #handling user information

    while True:
        name = input("Please enter the student's name (or type 'stop' to finish):")
        if name.lower() == 'stop':
            break 

    #checking whether the student name has duplication or not
           
        if any(student[1].lower() == name.lower() for student in students):
            print(f"Student '{name}' already exists.")
        else:
            students.append((student_id,name))
            student_id += 1

    #displaying the list of students in the database
    print('Complete list of the students in the Database')
    print(students)

    #detailed students information
    print("Detailed student list:")
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}")

    #Calculate and Display Statistics
    total_Studetns = len(students)
    total_name_length = sum(len(student[1]) for student in students)

    if students:
        longest_name = max(students, key=lambda x: len(x[1]))
        shortest_name = min(students, key=lambda x: len(x[1]))
    else:
        longest_name = shortest_name = None

    print(f'Total number of students: {total_Studetns}')
    print(f'Total length of all student names combined: {total_name_length} characters')

    if longest_name and shortest_name:
        print(f'Student with the longest name: {longest_name[1]} (ID: {longest_name[0]})')
        print(f'Student with the shortest name: {shortest_name[1]} (ID: {shortest_name[0]})')

    


manage_student_database()