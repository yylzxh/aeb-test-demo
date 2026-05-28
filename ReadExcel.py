import pandas as pd
read=pd.read_excel('aeb_scenarios.xlsx')
print(f"用例总数：{len(read)}")
print(read.head(10))
print(read["expected"].value_counts(dropna=False))



