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
        FROM '{DATA_FILE}'
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

def revenue_categories():
    return duckdb.sql(f"""
        SELECT
            category,
            SUM(revenue) AS total_revenue
        FROM '{DATA_FILE}' 
        GROUP BY category
        HAVING SUM(revenue) > 5000
        ORDER BY total_revenue DESC
    """)

def sort_order_size():
    return duckdb.sql(f"""
        SELECT
            order_id,
            revenue,
            CASE
                WHEN revenue >= 1000 THEN 'High'
                WHEN revenue >= 500 THEN 'Medium'
                ELSE 'Low' 
            END AS order_size
        FROM '{DATA_FILE}' 
    """)

def city_monthly_revenue():
    return duckdb.sql(f"""
        SELECT
            DATE_TRUNC('Month', date) AS month,
            city,
            SUM(revenue) AS revenue
        FROM '{DATA_FILE}' 
        GROUP BY month, city
        ORDER BY month, revenue DESC
    """)


if __name__ == "__main__":
    print("\n<--- Categories --->")
    print(show_categories())

    print("\n<--- Number of orders --->")
    print(count_orders())

    print("\n<--- Average revenue --->")
    print(average_revenue())

    print("\n<--- Top 10 orders --->")
    print(top_orders())

    print("\n<--- Revenue by city --->")
    print(revenue_by_city())

    print("\n<--- Category statistics --->")
    print(category_statistics())

    print("\n<--- Categories over 5000 --->")
    print(revenue_categories())

    print("\n<--- Order sizes --->")
    print(sort_order_size())

    print("\n<--- Monthly revenue per city --->")
    print(city_monthly_revenue())