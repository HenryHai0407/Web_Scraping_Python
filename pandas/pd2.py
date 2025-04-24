import pandas as pd
import numpy as np
import datetime
# data = {
#    "value": range(12),
#    "variable": ["A"] * 3 + ["B"] * 3 + ["C"] * 3 + ["D"] * 3,
#    "date": pd.to_datetime(["2020-01-03", "2020-01-04", "2020-01-05"] * 4)
# }

# df  = pd.DataFrame(data)

# pivoted = df.pivot(index="value",columns="date",values ="variable")
# print(pivoted)

# pivoted2 = pivoted.reset_index()
# print(pivoted2)

# Pivot Table
data = {
    "A": ["one","one","two","three"] * 6,
    "B": ["A","B","C"] * 8,
    "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
}

df = pd.DataFrame(data)

df2 = pd.pivot_table(df, values = ["D","F"], index=["A","B"], columns =["C"])


### melt()

cheese = pd.DataFrame({
    "first": ["John","Mary"],
    "last": ["Doe","Bo"],
    "height": [5.5,6.0],
    "weight": [130,150]
})

print(cheese)

cheese1 = cheese.melt(id_vars=["height","weight"])

cheese2 = cheese.melt(id_vars=["first","last"], var_name="quantity")


# Explode() for nested, list-like values
keys = ["panda1", "panda2", "panda3"]

values = [["eats", "shoots"], ["shoots", "leaves"], ["eats", "leaves"]]

df = pd.DataFrame({"keys": keys, "values":values})

df1 = df.explode("values")
print(df1)

df1.columns = df1.columns.str.upper()
print(df1)

