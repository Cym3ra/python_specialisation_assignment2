import duckdb
import matplotlib.pyplot as plt

DATA_FILE = "data/ecommerce_sales.csv"

def create_revenue_chart():
    result = duckdb.sql(f"""
        SELECT
            category,
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}' 
        GROUP BY category
        ORDER BY revenue DESC
    """).df()

    result.plot(
        x="category",
        y="revenue",
        kind="bar",
        legend=False
    )

    plt.title("Revenue per category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    create_revenue_chart()