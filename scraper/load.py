import os
from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set in environment")

engine = create_engine(DATABASE_URL)

def load_df(df: pd.DataFrame, table_name: str = 'quotes'):
    """
    Appends the DataFrame into the 'quotes' table.
    """
    # optional: add a scraped_at timestamp
    if 'scraped_at' not in df.columns:
        df['scraped_at'] = pd.Timestamp.now()
    df.to_sql(table_name, engine, if_exists='append', index=False)
