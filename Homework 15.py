
# import csv

# def add_student_to_csv(file_path, student_info):
    
#     try:
#         with open(file_path, 'r') as file:
#             csv.reader(file)
#     except FileNotFoundError:
#         with open(file_path, 'w', newline='') as file:
#             csv.writer(file).writerow(["id", "name", "age", "grade", "subject_name", "marks"])

   
#     with open(file_path, 'a', newline='') as file:
#         csv.writer(file).writerow(student_info)


# student_information = [3, "John Doe", 20, "A", "Math", 90]

# csv_file_path = "students.csv"
# add_student_to_csv(csv_file_path, student_information)


# 2------------------------------------------------------------------

# import csv

# def read_all_students(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             reader = csv.reader(file)
#             header = next(reader)  # Skip the header row
#             students = [row for row in reader]
#         return header, students
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#         return None

# def read_specific_student(file_path, student_id):
#     try:
#         with open(file_path, 'r') as file:
#             reader = csv.reader(file)
#             header = next(reader)  # Skip the header row
#             for row in reader:
#                 if int(row[0]) == student_id:
#                     return header, [row]
#         print(f"Student with ID {student_id} not found.")
#         return None
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#         return None


# csv_file_path = "students.csv"


# all_students_info = read_all_students(csv_file_path)
# if all_students_info:
#     header, all_students = all_students_info
#     print("All Students:")
#     print(header)
#     for student in all_students:
#         print(student)


# specific_student_info = read_specific_student(csv_file_path, 2)
# if specific_student_info:
#     header, specific_student = specific_student_info
#     print("\nSpecific Student:")
#     print(header)
#     print(specific_student[0])



# 3 -----------------------------------------------------------------------------

# import csv

# def update_student_score(file_path, student_id, subject_name, updated_score):
#     try:
#         with open(file_path, 'r') as file:
#             reader = csv.reader(file)
#             header = next(reader)  
#             rows = [row for row in reader]

#         found = False
#         for row in rows:
#             if int(row[0]) == student_id and row[4] == subject_name:
#                 row[5] = str(updated_score)
#                 found = True
#                 break

#         if found:
#             with open(file_path, 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(header)
#                 writer.writerows(rows)
#             print(f"Score updated for Student ID {student_id}, Subject: {subject_name}")
#         else:
#             print(f"Student ID {student_id} with Subject {subject_name} not found.")
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")


# csv_file_path = "students.csv"


# student_id_to_update = 2
# subject_to_update = "Math"
# new_score = 95

# update_student_score(csv_file_path, student_id_to_update, subject_to_update, new_score)