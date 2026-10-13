import pandas as pd

df = pd.read_csv("hockey_raw.csv")

all_years = set(range(df["year"].min(), df["year"].max() + 1))
present_years = set(df["year"].unique())
missing_years = sorted(all_years - present_years)

print("Минимальный год:", df["year"].min())
print("Максимальный год:", df["year"].max())
print("Отсутствующие годы:", missing_years)





