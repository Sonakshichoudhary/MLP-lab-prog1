import pandas as pd

data = pd.read_csv("C:\\Users\sonak\OneDrive\Desktop\MlP")

data.columns = data.columns.str.strip()

data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

print("CSV File Content:")
print(data)

print("\nActual column names:")
print(data.columns.tolist())

print("\nExtracted 'Name' column:")
print(data['Name'])

