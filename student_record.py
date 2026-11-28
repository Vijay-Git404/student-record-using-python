student_record={}
def add_student(name):
    if name in student_record:
        print(f"Student {name} already exists.")
    else:
        age=int(input("Enter student age: "))
        courses=input("Enter courses (comma-separated): ").split(",")
        student_record[name]={
            "age":age,
            "grades":set(),
            "courses":set(courses)
        }
        print(f"Student {name} added successfully.")
def add_grade(name):
    if name in student_record:
        grade=int(input("Enter grade to add: "))
        if grade < 0 or grade > 100:
            print("Invalid grade. Please enter a grade between 0 and 100.")
            return
        student_record[name]["grades"].add(grade)
        print(f"Grade {grade} added for student {name}.")
    else:
        print(f"Student {name} does not exist.")
def is_student_enrolled(name,course):
    if name in student_record:
        if course in student_record[name]["courses"]:
            print(f"Student {name} is enrolled in {course}.")
        else:
            print(f"Student {name} is not enrolled in {course}.")
    else:
        print(f"Student {name} does not exist.")
def calculate_average_grade(name):
    if name in student_record:
        grades=student_record[name]["grades"]
        if grades:
            average=sum(grades)/len(grades)
            print(f"Average grade for student {name} is {average:.2f}.")
        else:
            print(f"No grades available for student {name}.")
    else:
        print(f"Student {name} does not exist.")
def list_students_by_course(course):
    students=[]
    for name, info in student_record.items():
        if course in info["courses"]:
            students.append(name)
    print(f"Students enrolled in {course}: {', '.join(students)}")
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Check Enrollment")
    print("4. Calculate Average Grade")
    print("5. List Students by Course")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name=input("Enter student name: ")
        add_student(name)
    elif choice == '2':
        name=input("Enter student name: ")
        add_grade(name)
    elif choice == '3':
        name=input("Enter student name: ")
        course=input("Enter course name: ")
        is_student_enrolled(name, course)
    elif choice == '4':
        name=input("Enter student name: ")
        calculate_average_grade(name)
    elif choice == '5':
        course=input("Enter course name: ")
        list_students_by_course(course)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")