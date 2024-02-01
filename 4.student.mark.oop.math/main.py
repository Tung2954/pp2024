from domains import Student
from domains import Course
from input import number_of_students, number_of_courses, check_student_number, check_course_number, select_course
from output import list_students, list_courses, show_student_marks, list_of_choice, sort_students_by_gpa

students = []
courses = []

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
                        credits = selected_course.credits
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
            print("Not a legal step!!!")

if __name__ == "__main__":
    select_choice()
