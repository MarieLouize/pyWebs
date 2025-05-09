from scraper.fetch import fetch_all
from scraper.parse import parse_quotes
from scraper.load import load_df
import os

# let’s grab 3 pages for our smoke test
PAGES = 3

def run_etl():
    for page, html in fetch_all(PAGES):
        df = parse_quotes(html, page)
        print(f"Page {page} → {len(df)} quotes")
        load_df(df)

if __name__ == '__main__':
    # require DATABASE_URL in env
    if not os.getenv('DATABASE_URL'):
        print("Error: set DATABASE_URL in your .env and `source .env` first.")
    else:
        run_etl()
