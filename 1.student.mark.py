students = []
courses = []

def number_of_students():
    return int(input("Enter the number of student(s): "))

def info_students():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student dob: ")
    return {"id": student_id, "name": student_name, "dob": student_dob, "courses": []}

def number_of_courses():
    return int(input("Enter the number of course(s): "))

def info_courses():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_marks(course, student):
    marks = float(input(f"Enter the mark for {course['name']} of the student {student['info']['name']}: "))
    student['info']['courses'].append({"id": course['id'], "marks": marks})

def select_course():
    print("Select a course")
    list_courses()
    course_id = input("Enter the course ID: ")
    
    for course in courses:
        if course['id'] == course_id:
            return course

def list_students():
    print("List of students: ")
    for student in students:
        print(f"Student ID: {student['info']['id']} - Name: {student['info']['name']}")

def list_courses():
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course['id']} - Name: {course['name']}")    
        
def show_student_marks(student, course):
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
            selected_course = select_course()
            if selected_course:
                for student in students:
                    input_marks(selected_course, student)
            
        elif choice == 4:
            list_students()
        
        elif choice == 5:
            list_courses()
    
        elif choice == 6:
            selected_student_id = input("Enter the student ID to show marks: ")
            selected_student = next((student for student in students if student['info']['id'] == selected_student_id), None)

            if selected_student:
                show_student_marks(selected_student, selected_course)
            else:
                print(f"No student found with ID {selected_student_id}")
            
        elif choice == 7:
            return 0
        
num_student = number_of_students()
for _ in range(num_student):
    student_info = info_students()
    students.append({"info": student_info, "marks": {}})

num_course = number_of_courses()
for _ in range(num_course):
    course_info = info_courses()
    courses.append(course_info)
    
select_choice()