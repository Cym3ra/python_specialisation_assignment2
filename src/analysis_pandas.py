import pandas as pd

DATA_FILE = "data/ecommerce_sales.csv"

def _load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILE)


def revenue_by_category(data):
    return (
        data.groupby("category", as_index=False)["revenue"].sum()
        .rename(columns={"revenue": "total_revenue"})
        .sort_values("total_revenue", ascending=False)
    )

def category_summary(data):
    return(
        data.groupby("category")
        .agg(
            orders=("order_id", "count"),
            units=("units", "sum"),
            revenue=("revenue", "sum"),
            average_revenue=("revenue", "mean"),
            ).reset_index().sort_values("revenue", ascending=False)
    )

def city_category_revenue(data):
    return(
        data.groupby(["city", "category"], as_index=False)["revenue"]
        .sum().sort_values("revenue", ascending=False)
    )

def monthly_revenue(data):
    data = data.copy()

    data["date"] = pd.to_datetime(data["date"])

    return (
        data.groupby(data["data"].dt.to_period("M"))["revenue"].sum().reset_index()
    )


if __name__ == "__main__":
    print("\n**** Revenue per category ****")
    print(revenue_by_category(_load_data))

    print("\n**** Category summary ****")
    print(category_summary(_load_data))

    print("\n**** Revenue per city and category ****")
    print(city_category_revenue(_load_data))

    print("\n**** Monthly revenue ****")
    print(monthly_revenue(_load_data))
