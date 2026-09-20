import time
import statistics
import matplotlib.pyplot as plt
import pandas as pd

from analysis_pandas import (
    load_data,
    revenue_by_category as pandas_revenue_by_category,
    category_summary as pandas_category_summary,
    monthly_revenue as pandas_monthly_revenue,
)

from analysis_duckdb import (
    create_connection,
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
    con = create_connection()

    tests = [
        (
            "Revenue per category",
            lambda: pandas_revenue_by_category(data),
            lambda: duckdb_revenue_by_category(con),
        ),
        (
            "Category summary",
            lambda: pandas_category_summary(data),
            lambda: duckdb_category_summary(con),
        ),
        (
            "Monthly revenue",
            lambda: pandas_monthly_revenue(data),
            lambda: duckdb_monthly_revenue(con),
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


def plot_results(df: pd.DataFrame, out_path: str = "results/benchmark_tid.png") -> None:
    plot_df = df.set_index("test")[["pandas_seconds", "duckdb_seconds"]]
    plot_df.columns = ["Pandas", "DuckDB"]

    ax = plot_df.plot(kind="bar", figsize=(8, 5))
    ax.set_ylabel("Tid (sekunder)")
    ax.set_title("Pandas vs DuckDB – körtid per fråga (median av 10 körningar)")
    ax.legend(title="Metod")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)

    print(f"Diagram sparat till {out_path}")



if __name__ == "__main__":
    results = run_benchmark()

    print(results)

    results.to_csv(
        "results/benchmark_results.csv",
        index=False
    )

    print("\nBenchmark sparat till results/benchmark_results.csv")

    plot_results(results)
