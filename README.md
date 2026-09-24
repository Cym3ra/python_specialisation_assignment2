# DuckDB vs Pandas - ett fördjupningsprojekt i Python
- Inlämningsuppgift 2 

Ett litet projekt som utforskar DuckDB som ett komplement/alternativ till
Pandas för att läsa och analysera data i Python, samt tränar SQL.

## Projektet innehåller tre delar

1. **`analysis_duckdb.py` & `analysis_pandas.py`** – Samma analyser implementerade i både Pandas och DuckDB. 
2. **`benchmark.py`** - script som mäter tid för respektive analys, Pandas vs DuckDB.
3. **`sql_exercises.py`** – SQL-övningar mot samma data, till för att repetera SQL.
4. **`visualization.py`** – Ett exempel som visar DuckDB använt som ett
   utforskande analysverktyg där resultatet plottas som ett linjediagram.


## Installation

```bash
# skapa och aktivera en virtuell miljö (valfritt men rekommenderas)
python -m venv .venv

# aktivera venv i Windows
.venv\Scripts\activate

# installera nödvändiga program
pip install -r requirements.txt
```

## Körordning

Kör alltid från projektets rotmapp (`CarinaK_fördjupning_python/`):

```bash

# 1. Kör och jämför Pandas vs DuckDB (skriver resultat + diagram till results/)
python src/benchmark.py

# 2. Kör SQL-övningarna
python src/sql_exercises.py

# 3. Utforska data med DuckDB och skapa ett diagram
python python -m src.visualization
```

För att köra analyserna separat utan benchmark:
```bash
python src/analysis_duckdb.py
python src/analysis_pandas.py
```

## Data

CSV filen innehåller kolumnerna: order_id, city, date, category, price, units, revenue

## Resultat

Efter körning hamnar sparade resultat i `results/`:
- `benchmark_results.csv` – tid per fråga och metod
- `benchmark_tid.png` – stapeldiagram över körtider


## Sidnot

CSV-filen med 100k rader var för stor att pusha upp till github, 
så använder filen med 2500 rader för att logiken ska fungera.