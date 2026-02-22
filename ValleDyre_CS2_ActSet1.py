name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_subject = input("Enter your favorite subject: ")

student_record = {
    "Name": name,
    "Age": age,
    "Favorite Subject": favorite_subject
}

print("Student Record: ", student_record)
for key, value in student_record.items():
    print(f"  {key}: {value}")