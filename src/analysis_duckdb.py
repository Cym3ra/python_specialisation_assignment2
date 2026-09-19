import duckdb

DATA_FILE = "data/ecommerce_sales.csv"


def create_connection():
    return duckdb.connect()


def revenue_by_category(con):

    return con.execute(f"""
        SELECT
            category,
            SUM(revenue) AS total_revenue
        FROM '{DATA_FILE}'
        GROUP BY category
        ORDER BY total_revenue DESC
        """).df()

def category_summary(con):
    
    return con.execute(f"""
        SELECT
            category,
            COUNT(order_id) AS orders,
            SUM(units) AS units,
            SUM(revenue) AS revenue,
            AVG(revenue) AS average_revenue
        FROM '{DATA_FILE}'
        GROUP BY category
        ORDER BY revenue DESC
        """).df()

def city_category_revenue(con):

    return con.execute(f"""
        SELECT
            city,
            category,
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}'
        GROUP BY city, category
        ORDER BY revenue DESC
        """).df()

def monthly_revenue(con):

    return con.execute(f"""
        SELECT
            DATE_TRUNC('month', date) AS month
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}'
        GROUP BY month
        ORDER BY month
        """).df()


if __name__ == "__main__":
    print("\n---- Revenue per category ----")
    print(revenue_by_category(create_connection()))

    print("\n---- Category summary ----")
    print(category_summary(create_connection()))

    print("\n---- Revenue per city and category ----")
    print(city_category_revenue(create_connection()))

    print("\n---- Monthly revenue ----")
    print(monthly_revenue(create_connection()))