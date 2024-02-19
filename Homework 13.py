


my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

def display_student_details(data):
    
    student_ids = [str(student["id"]) for student in data["students"]]
    print("Student IDs: " + ", ".join(student_ids))

   
    selected_id = input("Enter the student ID: ")

  
    selected_student = next((student for student in data["students"] if str(student["id"]) == selected_id), None)

    if selected_student:
      
        print(f"\nStudent Information:\nID: {selected_student['id']}, Name: {selected_student['name']}, Age: {selected_student['age']}")

        
        for subject in data["subjects"]:
            grade = subject["grades"].get(str(selected_student["id"]), "N/A")
            print(f"Subject: {subject['name']}, Grade: {grade}")
    else:
        print("Student not found.")


display_student_details(my_dict)
