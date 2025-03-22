import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define possible class names
class_names = ["A", "B", "C", "D", "E"]

# Generate 20 students
students = []
for i in range(1, 21):  # 1 to 20
    student_id = f"S{i:03d}"  # Format: S001, S002, ...
    full_name = fake.name().split()
    surname = full_name[-1]  # Last word is surname
    first_name = " ".join(full_name[:-1])  # Rest is first name
    dob = fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%d-%m-%Y")
    score = round(random.uniform(50, 100), 2)  # Random score between 50-100
    student_class = random.choice(class_names)

    # Generate a properly formatted address: "Street Number Street Name City"
    address_parts = fake.address().split("\n")[0].split(",")  # Get only street address
    street = address_parts[0]  # Street number + name
    city = fake.city()
    address = f"{street} {city}"  # Final formatted address

    students.append(f"{student_id},{surname},{first_name},{dob},{score},{student_class},{address}")

# Write to student.txt
file_name = "student.txt"
with open(file_name, "w") as f:
    f.write("StudentID,Surname,FirstName,DateOfBirth,Score,Class,Address\n")  # Header
    f.write("\n".join(students))  # Write student data

print(f"File '{file_name}' generated successfully with 20 students!")
