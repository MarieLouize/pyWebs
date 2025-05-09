import requests
from typing import Generator, Tuple

BASE = "http://quotes.toscrape.com/page/{page}/"

def fetch_all(pages: int = 5) -> Generator[Tuple[int, str], None, None]:
    """
    Yield (page_number, html) for pages 1..pages.
    """
    for page in range(1, pages + 1):
        url  = BASE.format(page=page)
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        yield page, resp.text
