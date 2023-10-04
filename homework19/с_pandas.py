import pandas as pd

file_name = "pandas_adress.csv"
df = pd.read_csv(file_name)

num_teams = df.shape[0]
print("Кількість команд, що брали участь у Євро-2012:", num_teams)
