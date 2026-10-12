import pandas as pd
from pathlib import Path

file_path = Path(__file__).resolve().parent / "facilities.csv"
df = pd.read_csv(file_path)

text_columns = ['name', 'category', 'district']
df[text_columns] = df[text_columns].apply(lambda column: column.str.strip())
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df = df.dropna(subset=['name', 'category', 'district', 'quantity'])
df = df.drop_duplicates()

gulou_records = df.loc[(df['district'] == '鼓楼区') & (df['quantity'] >= 2)]
result = df.groupby('category')['quantity'].agg(['count', 'sum', 'mean'])
result = result.sort_values(by='sum', ascending=False)

print('鼓楼区数量不少于 2 的设施：')
print(gulou_records)
print('\n按类别统计：')
print(result)
