# Working with File in Python
#
file_name = "dictionary1\sinhvien.txt"

try:
    with open(file_name,"r") as f:
        reading_f = f.readline() # Read a first line
        reading_f1 = f.readline() # If we alreay run readline(), this line will read the NEXT line
        r2 = f.readlines() # Return a LIST of all sentences
        print(reading_f)
        print(f"-------------")
        print(reading_f1)
        print(r2)
except FileNotFoundError:
    print(f"Error: The file {file_name} does not exist")
except Exception as e:
    print(f"An error occurred: {e}")

