import duckdb

duckdb.read_csv("data/ecommerce_sales.csv")

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
