class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.courses = []

    def input_marks(self, course_id, marks):
        course = next((c for c in courses if c.id == course_id), None)
        if course:
            self.courses.append({"course": course, "marks": marks})
        else:
            print(f"Course with ID {course_id} not found.")

    def display_info(self):
        print(f"Student ID: {self.id} - Name: {self.name}")

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

students = []
courses = []

def number_of_students():
    return int(input("Enter the number of student(s): "))

def number_of_courses():
    return int(input("Enter the number of course(s): "))

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

def select_course(courses):
    print("Select a course ")
    list_courses(courses)
    course_id = input("Enter course ID: ")
    
    for course in courses:
        if course.id == course_id:
            return course
        
def list_students(students):
    print("List of students: ")
    for student in students:
        student.display_info()

def list_courses(courses):
    print("List of courses: ")
    for course in courses:
        print(f"Course ID: {course.id} - Name: {course.name}")
        
def show_student_marks(student, selected_course):
    print(f"Marks for {selected_course.name} - Student ID: {student.id} - Name: {student.name}")

    for course_mark in student.courses:
        if course_mark['course'].id == selected_course.id:
            print(f"Course ID: {course_mark['course'].id} - Marks: {course_mark['marks']}")
            return

    print(f"No marks found for {selected_course.name}")

def select_choice():
    while True:
        print(" ---------------------------------------")
        print("1. Enter the number and information of student(s).")
        print("2. Enter the number and information of course(s).")
        print("3. Enter mark for student(s).")
        print("4. List of student(s).")
        print("5. List of course(s).")
        print("6. Show student(s) mark.")
        print("7. Done.")

        choice = int(input("Enter the next step: "))

        if choice == 1:
            number_student = number_of_students()
            for _ in range(number_student):
                student_id = input("Enter student id: ")
                student_name = input("Enter student name: ")
                student_dob = input("Enter student dob: ")
                student = Student(student_id, student_name, student_dob)
                students.append(student)

        elif choice == 2:
            number_courses = number_of_courses()
            for _ in range(number_courses):
                course_id = input("Enter course id: ")
                course_name = input("Enter course name: ")
                course = Course(course_id, course_name)
                courses.append(course)

        elif choice == 3:
            selected_course = select_course(courses)
            if selected_course:
                for student in students:
                    marks = float(input(f"Enter the mark for {selected_course.name} of the student {student.name}: "))
                    student.input_marks(selected_course.id, marks)

        elif choice == 4:
            list_students(students)

        elif choice == 5:
            list_courses(courses)

        elif choice == 6:
            if check_student_number(students) and check_course_number(courses):
                selected_student_id = input("Enter the student ID to show marks: ")
                selected_student = next((student for student in students if student.id == selected_student_id), None)

                if selected_student:
                    selected_course = select_course(courses)
                    if selected_course:
                        show_student_marks(selected_student, selected_course)
                    else:
                        print("No course selected.")
                else:
                    print(f"No student found with ID {selected_student_id}")

        elif choice == 7:
            return 0

if __name__ == "__main__":
    select_choice()
