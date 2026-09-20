import duckdb

DATA_FILE = "data/ecommerce_sales_100k.csv"

def create_connection():
    con = duckdb.connect()
    con.execute(f"CREATE TABLE sales AS SELECT * FROM read_csv_auto('{DATA_FILE}')")
    return con

def revenue_by_category(con):

    return con.execute(f"""
        SELECT
            category,
            SUM(revenue) AS total_revenue
        FROM sales
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
        FROM sales
        GROUP BY category
        ORDER BY revenue DESC
        """).df()

def city_category_revenue(con):

    return con.execute(f"""
        SELECT
            city,
            category,
            SUM(revenue) AS revenue
        FROM sales
        GROUP BY city, category
        ORDER BY revenue DESC
        """).df()

def monthly_revenue(con):

    return con.execute(f"""
        SELECT
            DATE_TRUNC('month', date) AS month,
            SUM(revenue) AS revenue
        FROM sales
        GROUP BY month
        ORDER BY month
        """).df()


if __name__ == "__main__":

    conn= create_connection()
    print("\n---- Revenue per category ----")
    print(revenue_by_category(conn))

    print("\n---- Category summary ----")
    print(category_summary(conn))

    print("\n---- Revenue per city and category ----")
    print(city_category_revenue(conn))

    print("\n---- Monthly revenue ----")
    print(monthly_revenue(conn))