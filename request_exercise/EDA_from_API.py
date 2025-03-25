import requests
import pandas as pd
from sqlalchemy import create_engine

# Request Data from API

def fetch_api_data(url,params=None, headers=None):
    """
    Request data from the API and return JSON response.
    Includes error handling and a timeout.
    """
    try:
        response = requests.get(url,params=params, headers=headers, timeout=10)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except Exception as error:
        print(f"An error occurred:{error}")
        return None

# Example API endpoint and parameters
api_url = "https://api.example.com/messy-data"
params = {"date": "2023-01-01"}
headers = {"Authorization": "Bearer YOUR_API_KEY"}

raw_data = fetch_api_data(api_url, params=params, headers=headers)
if raw_data is None:
    print("Failed to fetch data from the API.")
    exit()

# Step 2: Clean and Transform the Messy JSON Data
# Suppose raw_data is a list of dictionaries that might look like this:
# [
#   {
#       "id": 1,
#       "name": "  John Doe  ",
#       "date": "2023-01-01T12:34:56Z",
#       "details": {"score": " 85 ", "remarks": " good "}
#   },
#   { ... },
#   ...
# ]

df = pd.json_normalize(raw_data)

# Advanced cleaning:
#1 Trim extra whitespace in string columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

#2 Convert date columns to datetime (if they exist)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"],errors="coerce")

#3 Convert numeric fields (e.g the score inside a nested dict)
if "details.score" in df.columns:
    df["details.score"] = pd.to_numeric(df["details.score"],errors="coerce")

#4 Rename columns for clarity
df.rename(columns={
"id": "record_id",
    "name": "full_name",
    "details.score": "score",
    "details.remarks": "remarks"
})

#5 Drop rows that are missing critical data
df.dropna(subset=["record_id","full_name","score"], inplace=True)  

#6 Print DataFrame to check the updates
print(f" Transformed Data: {df.head()}")

### Step 3: Load Data into Database
connection_string = "postgresql://username:password@localhost:5432/mydatabase"
engine = create_engine(connection_string)

# Write the DataFrame to the database table "cleaned_data"
# if_exists="replace" drops the existing table, or you can use "append" to add new records.
df.to_sql("cleaned_data", engine, if_exists="replace", index=False)

print("Data loaded successfully into the data warehouse.")


# Explanation for params in getting_API():
# Using params when we need: filtering API data, paginating results, sorting results, and providing authentication tokens
