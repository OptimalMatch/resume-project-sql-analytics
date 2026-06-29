"""Milestone 2: load a CSV dataset into PostgreSQL.

Set DATABASE_URL in .env, drop your dataset in data/, and run: python load.py
"""
import os
import pandas as pd
from sqlalchemy import create_engine  # or psycopg2 directly

DB = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/analytics")


def main():
    df = pd.read_csv("data/dataset.csv")     # TODO: your real dataset
    # TODO milestone 3: clean nulls/types/duplicates here, and note what you changed
    create_engine(DB).connect()              # TODO: df.to_sql("raw", engine, if_exists="replace")
    print(f"loaded {len(df)} rows (wire up to_sql)")


if __name__ == "__main__":
    main()
