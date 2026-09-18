import pandas as pd

data = pd.read_csv("data/ecommerce_sales.csv")

result = (
    data.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(result)