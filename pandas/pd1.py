import pandas as pd

mydataset = {
    'car': ["BMW","Volvo","Ford"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(mydataset)
# print(myvar)

# print(pd.__version__)

# print(myvar.iloc[0])

data1 = {
    'Name': ['Ninja_1','Ninja_2','Ninja_3','Ninja_4'],
    'Department': ['Marketing','Sales','Marketing','Engineering'],
    'Salary': [50000,60000,55000,70000]
}

df1 = pd.DataFrame(data1)
# print(df)
# Select multiple columns
# print(df.loc[:,['Name','Salary']])
# Select a subset of rows and columns
# subset = df.loc[df['Department'] == 'Marketing',['Name','Salary']]
# print(subset)
# Update a Value
# df.loc[1,'Salary'] = 65500
# print(df)

# Select multiple values/ or update multiple values
# value1 = df.loc[[0,3],'Salary'] = 100000
# print(df)

### -----
# iloc.
# row = df.iloc[[1,3],[0,2]]
# print(row)

# updated_value = df.iloc[1,1] =  100
# print(updated_value)
# print(df)

# Slicing
print(df1.iloc[0:3,0:2])
            