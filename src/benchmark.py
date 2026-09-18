import time
import statistics

import pandas as pd
import duckdb

from analysis_pandas import (
    load_data,
    revenue_by_category as pandas_revenue_by_category,
    category_summary as pandas_category_summary,
    monthly_revenue as pandas_monthly_revenue,
)

from analysis_duckdb import (
    revenue_by_category as duckdb_revenue_by_category,
    category_summary as duckdb_category_summary,
    monthly_revenue as duckdb_monthly_revenue,
)


NUMBER_OF_RUNS = 10


def measure(function, number_of_runs=NUMBER_OF_RUNS):
    times = []

    for _ in range(number_of_runs):
        start = time.perf_counter()
        function()

        end = time.perf_counter()
        times.append(end - start)

    return statistics.median(times)


def run_benchmark():
    data = load_data()

    tests = [
        (
            "Revenue per category",
            lambda: pandas_revenue_by_category(data),
            duckdb_revenue_by_category,
        ),
        (
            "Category summary",
            lambda: pandas_category_summary(data),
            duckdb_category_summary,
        ),
        (
            "Monthly revenue",
            lambda: pandas_monthly_revenue(data),
            duckdb_monthly_revenue,
        ),
    ]

    results = []

    for name, pandas_function, duckdb_function in tests:
        pandas_time = measure(pandas_function)
        duckdb_time = measure(duckdb_function)

        results.append(
            {
                "test": name,
                "pandas_seconds": pandas_time,
                "duckdb_seconds": duckdb_time,
            }
        )

    return pd.DataFrame(results)


if __name__ == "__main__":
    results = run_benchmark()

    print(results)

    results.to_csv(
        "results/benchmark_results.csv",
        index=False
    )

    print("\nBenchmark sparat till results/benchmark_results.csv")
