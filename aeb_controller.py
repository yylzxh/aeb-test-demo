#存放被测功能
def should_break(speed,distance):
    if speed > 60 and distance < 10:
        return True
    return False
# import pandas as pd
# df = pd.read_excel("aeb_scenarios.xlsx")
# print(f"用例总数: {len(df)}")
# print(df.head(10))
# print(df["expected"].value_counts(dropna=False))
