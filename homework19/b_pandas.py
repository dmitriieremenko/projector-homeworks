import pandas as pd

file_name = "pandas_adress.csv"
df = pd.read_csv(file_name)

selected_columns = df[["Team", "Yellow Cards", "Red Cards"]]
print(selected_columns)
