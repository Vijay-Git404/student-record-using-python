student_record={}
def add_student(name,age,courses):
    if name in student_record:
        print(f"Student {name} already exists.")
    else:
        student_record[name]={
            "age":age,
            "grades":set(),
            "courses":set(courses)
        }
        print(f"Student {name} added successfully.")
add_student("John Doe", 20, ["Math", "Science"])
print(student_record)