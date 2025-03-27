import csv

def eligible_score(a,b,c):
    try:
        x = (a*2+b+c)*3/4
        return x
    except Exception as e:
        print(f"Wrong input!")
        return None

passed_student = []
file_name = "exception\\score.csv"
try:
    with open(file_name) as f:
        f = csv.DictReader(f)
        for student in f:
            try:
                first_score = float(student['score1'])
                second_score = float(student['score2'])
                third_score = float(student['score3'])
                x = eligible_score(first_score,second_score,third_score)
                if x is not None and x >= 26:
                    passed_student.append(student['fullname'])
                # Intentionally made a mistake in "Pham Thanh Hoang" student to run below exception
            except ValueError:
                print(f"Error: Invalid score format in CSV for student {student['fullname']}. Please check the file.")
except FileNotFoundError:
    print(f"Error: The file {file_name} was not found")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


if passed_student:
    print(", ".join(passed_student), f"is/are eligible students for this university!")
else:
    print("No eligible students!")