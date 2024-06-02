import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|', index_col='user_id')

print("--------First 10 entries -------")
print(users.head(10))
print("--------Last 10 entries -------")
print(users.tail(10))

print("\nNumber of Observations:", len(users))
print("Number of Columns:", len(users.columns))
print("Print the name of all the columns:")
print(users.columns)

print("\nHow is the dataset indexed?")
print(users.index)

print("\nWhat is the data type of each column?")
print(users.info())

print("\nPrint only the occupation column:")
print(users['occupation'])

print("\nHow many different occupations are in this dataset?")
print(users['occupation'].nunique())

print("\nWhat is the most frequent occupation?")
print(users['occupation'].mode())

print("\nDataFrame Info.")
print(users.info())

print("\nDescribe all the columns:")
print(users.describe())

print("\nSummarize only the occupation column:")
print(users['occupation'].value_counts())

print("\nWhat is the mean age of users?")
print(users['age'].mean())

print("\nWhat is the age with least occurrence?")
print(users['age'].value_counts().idxmin())