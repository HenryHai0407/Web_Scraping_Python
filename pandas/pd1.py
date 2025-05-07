import pandas as pd
import matplotlib.pyplot as plt

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

####
calories = {'day1':420, 'day2': 500, 'day3': 600}

myvar1 = pd.Series(calories)

# print(myvar1)

myvar2 = pd.Series(calories, index = ['day1','day2'])

#print(myvar2)

### Replace using Mean, Median, or Mode
## For example you have df as dataframe
## x = df['Calories'].mean()
## df.fillna({'Calories': x}, inplace = True)
## inplace means that the value will replace the original dataframe, not creating a new dataframe.

dataset = {
    'Duration': [55,60,65,70,75,80,85,90],
    'Date': ['2020/12/01','2020/12/02','2020/12/03','2020/12/04','2020/12/05','2020/12/06','2020/12/07','2020/12/08'],
    'Pulse': [110,117,103,109,117,98,103,100],
    'Maxpulse': [130,145,135,175,148,147,138,125],
    'Calories': [409.1,479.0,340.0,282.4,406.0,300.0,374.0,253.3]
}

df2 = pd.DataFrame(dataset)
print(df2)
df2['Date']= pd.to_datetime(df2['Date'], format = 'mixed')
print(df2)

# Removing rows with NA
df2.dropna(subset=['Date'], inplace = True)

# Replacing Values
# df2.loc[1,'Calories'] = 579
# print(df2)

# Loop through data column
for x in df2.index:
    if df2.loc[x,"Duration"] > 80:
        df2.loc[x,"Duration"] = 79
print(df2)

# Removing Duplicates
print(df2.duplicated())
df2.drop_duplicates(inplace = True)

# Pandas correlation
# What is a good correlation? at least 0.6 <<<< to call it a good correlation.

# print(df2.corr())

# Plot
# Scatter
# df2.plot(kind = 'scatter', x = 'Pulse', y = 'Calories')
# plt.show()

# df2['Pulse'].plot(kind = 'hist')
# plt.show()

### Assigning data
# top5_rank_revenue['year_founded'] = 0

### Update the CEO of Dow Chemical to Jim Fitterling
# f500.loc['Dow Chemical','ceo'] = 'Jim Fitterling'
# Dow Chemical is row label
# ceo is column label

# Replace various variables
# df.replace([1,3],['one','three'])

# Rename columns
# df.rename(columns={'old_name': 'new_name'})

# Mass renaming of columns
# df.rename(columns=lambda x: x + 1)

