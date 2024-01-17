import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.courses = []

    def input_marks(self, course_id, marks, credits):
        rounded_marks = math.floor(marks)
        self.courses.append({"course_id": course_id, "marks": rounded_marks, "credits": credits})

    def calculate_gpa(self):
        total_credits = 0
        total_mark = 0
        
        for course in self.courses:
            total_credits += (course["credits"])
            total_mark += course["marks"]

        if total_credits == 0:
            return 0
        return total_mark / total_credits

    def display_info(self):
        print(f"Student ID: {self.id} - Name: {self.name} - GPA: {self.calculate_gpa()}")

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

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
    print("Select a course: ")
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
            print(f"Course ID: {course.id} - Name: {course.name} - Credits: {course.credits}")

def show_student_marks(student, selected_course):
    if check_student_number(students) and check_course_number(courses):
        print(f"Mark for {selected_course.name} - Course ID: {selected_course.id} - Credits: {selected_course.credits}")
        for _ in student.courses:
            if _['course_id'] == selected_course.id:
                print(f"Student ID: {student.id} - Name: {student.name} - Marks: {_['marks']}")
                return
        print(f"No marks found for {selected_course.name}")

def sort_students_by_gpa(students):
    return sorted(students, key=lambda x: x.calculate_gpa(), reverse=True)

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

def select_choice():
    while True:
        list_of_choice()
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
                course_credits = int(input("Enter course credits: "))
                course = Course(course_id, course_name, course_credits)
                courses.append(course)

        elif choice == 3:
            if check_student_number(students) and check_course_number(courses):
                selected_course = select_course(courses)
                if selected_course:
                    for student in students:
                        marks = float(input(f"Enter the mark for {selected_course.name} of the student {student.name}: "))
                        credits = select_course.credits
                        student.input_marks(selected_course.id, marks, credits)

        elif choice == 4:
            if check_student_number(students):
                list_students(students)

        elif choice == 5:
            if check_course_number(courses):
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
            if check_student_number(students) and check_course_number(courses):
                students_sorted = sort_students_by_gpa(students)
                list_students(students_sorted)

        elif choice == 8:
            break
        
        else:
            print("Not legal step!!!")

select_choice()