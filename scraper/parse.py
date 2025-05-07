from bs4 import BeautifulSoup
import pandas as pd

def parse_quotes(html: str, page: int) -> pd.DataFrame:
    """
    Parses all quotes on a page into a DataFrame with columns:
      - page (int)
      - quote (str)
      - author (str)
      - tags (list[str])
    """
    soup = BeautifulSoup(html, 'lxml')
    rows = []
    for box in soup.select('.quote'):
        text   = box.find('span', class_='text').get_text(strip=True)
        author = box.find('small', class_='author').get_text(strip=True)
        tags   = [t.get_text(strip=True) for t in box.select('.tags a.tag')]
        rows.append({
            'page':  page,
            'quote': text,
            'author': author,
            'tags':  ",".join(tags),
        })
    return pd.DataFrame(rows)
