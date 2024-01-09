students = []
courses = []

def check_student_number(students):
    if len(students) == 0:
        print("There is no student yet!")
        return False
    else:
        return True

def check_course_number(courses):
    if len(courses) == 0:
        print("There is no course yet!")
        return False
    else:
        return True
    
def number_of_students():
    return int(input("Enter the number of student(s): "))

def check_unique_id_student(student_id):
    return all(student['info']['id'] != student_id for student in students)

def info_students():
    while True:
        student_id = input("Enter student id: ")
        if check_unique_id_student(student_id):
            break
        else:
            print("Already have ID. Enter another one.")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student dob: ")
    return {"id": student_id, "name": student_name, "dob": student_dob, "courses": []}

def number_of_courses():
    return int(input("Enter the number of course(s): "))

def check_unique_id_course(course_id):
    return all(course['info']['id'] != course_id for course in courses)

def info_courses():
    while True:
        course_id = input("Enter course id: ")
        if check_unique_id_course(course_id):
            break
        else:
            print("Already have ID. Enter another one.")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_marks(course, student, students, courses):
    if not check_student_number(students) and not check_course_number(courses):
        print("There is no student and no course yet!")
    elif not check_student_number(students):
        print("There is no student yet!")
    elif not check_course_number(courses):
        print("There is no course yet!")
    else:
        marks = float(input(f"Enter the mark for {course['name']} of the student {student['info']['name']}: "))
        student['info']['courses'].append({"id": course['id'], "marks": marks})

def select_course(courses):
    if check_course_number(courses):
        print("Select a course")
        list_courses()
        course_id = input("Enter the course ID: ")
    
        for course in courses:
            if course['id'] == course_id:
                return course

def list_students(students):
    if check_student_number(students):
        print("List of students: ")
        for student in students:
            print(f"Student ID: {student['info']['id']} - Name: {student['info']['name']}")

def list_courses(courses):
    if check_course_number(courses):
        print("List of courses: ")
        for course in courses:
            print(f"Course ID: {course['id']} - Name: {course['name']}")    
        
def show_student_marks(student, course, students, courses):
        student_id = student['info']['id']
        course_id = course['id']
    
        for student_course in student['info']['courses']:
            if student_course['id'] == course_id:
                print(f"Mark for student name {student['info']['name']} in course {course['name']}: {student_course['marks']}")
                return

def list_of_choice():
    print(" ---------------------------------------")
    print("1.Enter the number and information of student(s).")
    print("2.Enter the number and information of course(s).")
    print("3.Enter mark for student(s).")
    print("4.List of student(s).")
    print("5.List of course(s).")
    print("6.Show student(s) mark.")
    print("7.Done.")

def select_choice():
    while True:
        list_of_choice()
        choice = int(input("Enter the next step: "))
        if choice == 1:
            number_student = number_of_students()
            for _ in range(number_student):
                student_info = info_students()
                students.append({"info": student_info, "marks": {}})
            
        elif choice == 2:
            number_courses = number_of_courses()
            for _ in range(number_courses):
                course_info = info_courses()
                courses.append(course_info)
            
        elif choice == 3:
            selected_course = select_course(courses)
            if selected_course:
                for student in students:
                    input_marks(selected_course, student)
            
        elif choice == 4:
            list_students(students)
        
        elif choice == 5:
            list_courses(courses)
    
        elif choice == 6:
            if check_student_number(students) and check_course_number(courses):
                selected_student_id = input("Enter the student ID to show marks: ")
                selected_student = next((student for student in students if student['info']['id'] == selected_student_id), None)

                if selected_student:
                    show_student_marks(selected_student, selected_course)
                else:
                    print(f"No student found with ID {selected_student_id}")
            
        elif choice == 7:
            return 0
        
select_choice()