import matplotlib.pyplot as plt

from src.analysis_duckdb import create_connection

"""
För att köra filen - från projektets rotmapp:
    py -m src.visualization
"""


DATA_FILE = "data/ecommerce_sales_100k.csv"

def create_revenue_chart():
    con = create_connection()
    result = con.execute(f"""
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