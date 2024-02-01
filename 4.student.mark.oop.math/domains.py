import math

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
