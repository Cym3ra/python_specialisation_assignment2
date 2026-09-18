import duckdb

DATA_FILE = "data/ecommerce_sales.csv"

#duckdb.sql("SELECT * FROM 'data/ecommerce_sales.csv'")

#duckdb.sql("SELECT 42").show()

# result = duckdb.sql("""
#     SELECT *
#     FROM 'data/ecommerce_sales.csv'
# """)

# print(result)

# result = duckdb.sql("""
#     SELECT
#         category,
#         SUM(units * price) AS total_sales
#     FROM 'data/ecommerce_sales.csv'
#     GROUP BY category
#     ORDER BY total_sales DESC
# """)

# print(result.df())

result = duckdb.sql("""
    SELECT
        category,
        SUM(units) AS quantity,
        SUM(revenue) AS revenue
    FROM 'data/ecommerce_sales.csv'
    WHERE units > 0
    GROUP BY category
""")


print(result)

def revenue_by_category():
    return duckdb.sql(f"""
        SELECT
            category,
            SUM(revenue) AS total_revenue
        FROM '{DATA_FILE}'
        GROUP BY category
        ORDER BY total_revenue DESC
        """).df()

def category_summary():
    return duckdb.sql(f"""
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

def city_category_revenue():
    return duckdb.sql(f"""
        SELECT
            city,
            category,
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}'
        GROUP BY city, category
        ORDER BY revenue DESC
        """).df()

def monthly_revenue():
    return duckdb.sql(f"""
        SELECT
            DATE_TRUNC('month', date) AS month
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}'
        GROUP BY month
        ORDER BY month
        """).df()

