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
    for course in courses:
        print(f"Course ID: {course.id} - Name: {course.name} - Credits: {course.credits}")
    course_id = input("Enter course ID: ")

    for course in courses:
        if course.id == course_id:
            return course
