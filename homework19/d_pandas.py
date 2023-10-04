import pandas as pd

file_name = "pandas_adress.csv"
df = pd.read_csv(file_name)

filtered_teams = df[df["Goals"] > 6]
print(filtered_teams)
