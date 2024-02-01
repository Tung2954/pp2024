from input import check_student_number, check_course_number

students = []
courses = []

def list_students(students):
    print("List of students: ")
    for student in students:
        student.display_info()

def list_courses(courses):
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course.id} - Name: {course.name} - Credits: {course.credits}")

def show_student_marks(student, selected_course):
    if check_student_number(students) and check_course_number(courses):
        print(f"Mark for {selected_course.name} - Course ID: {selected_course.id} - Credits: {selected_course.credits}")
        for _ in student.courses:
            if _['course_id'] == selected_course.id:
                print(f"Student ID: {student.id} - Name: {student.name} - Marks: {_['marks']}")
                return
        print(f"No marks found for {selected_course.name}")

def list_of_choice():
    print(" ---------------------------------------")
    print("1. Enter the number and information of student(s).")
    print("2. Enter the number and information of course(s).")
    print("3. Enter mark for student(s).")
    print("4. List of student(s).")
    print("5. List of course(s).")
    print("6. Show student(s) mark.")
    print("7. Sort student by GPA.")
    print("8. End")