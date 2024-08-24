'''' Instructions: Implement Python programs to accomplish the following task

Task

You are tasked with developing a Python program to manage a student database. The user should be able to add new students or stop the input process by entering "stop." Each student's name, along with a sequentially generated ID starting from 1, should be stored in a tuple, with these tuples kept in a list. The program must check for duplicate names before adding a new student and display a message if a duplicate is found. After the input process ends, the program should first display the complete list of student tuples and then display each student's ID and name individually. Additionally, the program should show the total number of students, calculate and display the total length of all student names combined, and identify the student with the longest and shortest name using appropriate operators. Implement these operations within a function named manage_student_database() and ensure you call this function at the end of your code.
'''
def manage_student_database():
    student_list = []
    student_id = 1

    # Simulated input list
    simulated_input = ["Alice", "Bob", "Charlie", "Alice", "Diana", "stop"]
    
    for name in simulated_input:
        if name.lower() == 'stop':
            break
        
        if any(student[1].lower() == name.lower() for student in student_list):
            print(f"Duplicate name '{name}' found. Please enter a different name.")
        else:
            student_list.append((student_id, name))
            student_id += 1
    print("\nComplete list of students:")
    for student in student_list:
        print(student)
    
    
    print("\nIndividual student details:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")
    
    
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {total_name_length}")
    
    if student_list:
        longest_name_student = max(student_list, key=lambda student: len(student[1]))
        shortest_name_student = min(student_list, key=lambda student: len(student[1]))
        
        print(f"Student with the longest name: ID: {longest_name_student[0]}, Name: {longest_name_student[1]}")
        print(f"Student with the shortest name: ID: {shortest_name_student[0]}, Name: {shortest_name_student[1]}")
    else:
        print("No students in the list.")


manage_student_database()
