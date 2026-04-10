import pandas as pd
# Ex-1
# data = [10,20,30,40,50]
# used to convert list to tabular data
# res = pd.Series(data)
# print(res)

# Ex-2
# data = {
#     "Name" : ["Std1","Std2","Std3","Std4","Std5"],
#     "Marks" : [60,70,80,90,100]
# }
# res = pd.DataFrame(data)
# print(res)

# Ex-3
#df = pd.read_csv("students.csv")
#print(df)
#print(df.head()) # display first 5 records
#print(df.tail())  # diaply last 5 records
#print(df.shape) #(10, 4) rows, cols
#print(df.columns) # display col names
#print(df.info()) # structure
#print(df.describe()) # statistics

#Ex-4
#df = pd.read_csv("students.csv")
#print(df["Name"]) # Name col
#print(df[["Name","Marks"]]) # multiple cols
#print(df[df["Marks"]>85])
#print(df[( (df["Marks"]>80) & (df["Marks"]<90) )])

#Ex-5
# df = pd.read_csv("students.csv")
# print(df.loc[0]) #display 0th row
# print(df.loc[0:2]) #0,1,2 rows (3rows)
# print(df.loc[[0,2,4]])


# Ex-6
# data = {
#     "Name" : ["Ravi","Sita","John"],
#     "Marks": [85,90,78]
# }
# df = pd.DataFrame(data)
# print(df.iloc[0]) # 0th Row
# print(df.iloc[0:2]) # 0 will include and 2 will exclude
# print(df.iloc[[0,2]]) # multiple rows

# print(df.iloc[0,1])
# print(df.loc[0,"Marks"])

# Ex-7
# data = {
#     "Name" : ["Ravi","Sita","John"],
#     "Marks": [85,90,78]
# }
# df = pd.DataFrame(data)
# df["Grade"] = ["A+","A++","A"]
# df["Marks"] = df["Marks"] + 10
# print(df)

# Ex-8
# df = pd.read_csv("pandas_nulls.csv")
# print(df.isnull())
# print(df.notnull())
# print(df.dropna())
# print(df.fillna(100))

# Ex-9
# df = pd.read_csv("students.csv")
# print(df.sort_values("Marks"))                  #Ascending
# print(df.sort_values("Marks",ascending=False))  #Decending

# Ex-10
# data = {
#     "Dept" : ["IT","IT","HR","HR"],
#     "Salary" : [50000,60000,45000,40000]
# }
# df = pd.DataFrame(data)
# print(df.groupby("Dept")["Salary"].sum())
# print(df.groupby("Dept")["Salary"].mean())
# print(df.groupby("Dept")["Salary"].max())
# print(df.groupby("Dept")["Salary"].min())

# Ex-11
# df1 = pd.DataFrame({
#     "ID" : [101,102],
#     "Name" : ["Std1","Std2"]
# })

# df2 = pd.DataFrame({
#     "ID" : [101,102],
#     "Marks":[90,95]
# })

# print( pd.merge(df1,df2,on="ID") )

# Ex-12
# df = pd.read_csv("students.csv")
# df["Marks"] = df["Marks"].apply(lambda x:x+10)
# print(df)

# Ex-13
# df = pd.read_csv("students.csv")
# print( df["Marks"].value_counts() )

# Ex-14
data = {
    "Name" : ["Ravi","Sita","John","Ravi"],
    "Dept" : ["IT","HR","IT","IT"],
    "Marks" : [85,90,None,85]
}
df = pd.DataFrame(data)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df.drop_duplicates().groupby("Dept")["Marks"].mean())