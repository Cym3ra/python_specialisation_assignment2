import duckdb

DATA_FILE = "data/ecommerce_sales.csv"

def show_categories():
    return duckdb.sql(f"""
        SELECT DISTINCT category
        FROM '{DATA_FILE}'
        ORDER BY category
    """)

def count_orders():
    return duckdb.sql(f"""
        SELECT COUNT(*) AS number_of_orders
        FROM '{DATA_FILE}
    """)

def average_revenue():
    return duckdb.sql(f"""
        SELECT AVG(revenue) AS average_revenue
        FROM '{DATA_FILE}' 
    """)

def top_orders():
    return duckdb.sql(f"""
        SELECT
            order_id,
            city,
            category,
            revenue
        FROM '{DATA_FILE}' 
        ORDER BY revenue DESC
        LIMIT 10
    """)

def revenue_by_city():
    return duckdb.sql(f"""
        SELECT
            city,
            SUM(revenue) AS total_revenue
        FROM '{DATA_FILE}' 
        GROUP BY city
        ORDER BY total_revenue DESC
    """)

def category_statistics():
    return duckdb.sql(f"""
        SELECT
            category,
            COUNT(*) AS orders,
            SUM(units) AS total_units,
            SUM(revenue) AS total_revenue,
            AVG(revenue) AS average_revenue,
            MIN(revenue) AS minimum_revenue,
            MAX(revenue) AS maximum_revenue
        FROM '{DATA_FILE}' 
        GROUP BY category
        ORDER BY total_revenue DESC
    """)