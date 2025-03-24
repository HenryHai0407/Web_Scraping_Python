import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Prepare a dictionary to store data for each column
data = {
    'id': [],
    'fullname': [],
    'dateofbirth': [],
    'gender': [],
    'address': [],
    'score': []
}

# Define possible gender options
genders = ['Male', 'Female', 'Other']

# Generate 40 rows of data
for i in range(1, 41):
    # ID: Sequential numbers from 1 to 40
    data['id'].append(i)
    
    # Gender: Randomly choose from 'Male', 'Female', 'Other'
    gender = random.choice(genders)
    data['gender'].append(gender)
    
    # Fullname: Generate first name based on gender, then add a last name
    if gender == 'Male':
        first_name = fake.first_name_male()
    elif gender == 'Female':
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name()  # Gender-neutral name
    last_name = fake.last_name()
    fullname = f"{first_name} {last_name}"
    data['fullname'].append(fullname)
    
    # Date of Birth: Random date for ages 18 to 60
    data['dateofbirth'].append(fake.date_of_birth(minimum_age=18, maximum_age=60))
    
    # Address: Random full address
    data['address'].append(fake.address())
    
    # Score: Random float between 0 and 100 with one decimal place
    data['score'].append(round(random.uniform(0, 100), 1))

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file without the index column
df.to_csv('accounts.csv', index=False)

print("CSV file 'accounts.csv' has been generated successfully!")