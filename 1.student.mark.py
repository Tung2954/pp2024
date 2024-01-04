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
    marks = float(input(f"Enter the mark for {course['name']} for the student {student['info']['name']}: "))
    student['info']['courses'].append({"id": course['id'], "marks": marks})

def select_course():
    print("Select a course:")
    list_courses()
    course_id = input("Enter the course ID: ")
    
    for course in courses:
        if course['id'] == course_id:
            return course

def list_students():
    print("List of students: ")
    for student in students:
        print(f"{student['info']['id']}, {student['info']['name']}")

def list_courses():
    print("List of courses: ")
    for course in courses:
        print(f"{course['id']}, {course['name']}")
        
def show_student_marks(student, course):
    student_id = student['info']['id']
    course_id = course['id']
    
    for student_course in student['info']['courses']:
        if student_course['id'] == course_id:
            print(f"Mark for student ID {student_id} in course ID {course_id}: {student_course['marks']}")
            return

    print(f"No marks found for student ID {student_id} in course ID {course_id}")

num_student = number_of_students()
for _ in range(num_student):
    student_info = info_students()
    students.append({"info": student_info, "marks": {}})

num_course = number_of_courses()
for _ in range(num_course):
    course_info = info_courses()
    courses.append(course_info)

selected_course = select_course()

if selected_course:
    for student in students:
        input_marks(selected_course, student)

    selected_student_id = input("Enter the student ID to show marks: ")
    selected_student = next((student for student in students if student['info']['id'] == selected_student_id), None)

    if selected_student:
        show_student_marks(selected_student, selected_course)
    else:
        print(f"No student found with ID {selected_student_id}")

list_courses()
list_students()
