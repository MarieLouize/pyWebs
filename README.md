# webscraper 


### Tree structure
```
├── data/              # raw CSV/HTML dumps (archival only)
├── notebooks/         # exploration & model prototyping
├── scraper/           # your scraping code
│   ├── fetch.py       # HTTP requests or Scrapy spiders
│   ├── parse.py       # HTML→structured dicts
│   └── load.py        # push into TimescaleDB
├── models/            # feature engineering + prediction code
├── tests/             # smoke and unit tests
├── main.py            # orchestration CLI or scheduler entrypoint
├── docker-compose.yml 
├── .env   
└── requirements.txt
```

# Start your database (and Adminer UI)
  From your project root:
  ```
  docker-compose pull        
  docker-compose up -d        
  ```
  You can now connect at:
  ```
  DATABASE_URL
  ```
# Verify the DB schema with Adminer
  1. Open your browser to: http://localhost:8080
  2. Log in with:
  * System: PostgreSQL
  * Server: db
  * Username / Password / Database: from your .env
  3. In the left sidebar you should see the quotes table.
  4. Click Structure → confirm columns (page, quote, author, tags, scraped_at).

#  Create & activate your Python virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

# Install Python dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install 
```
### Load environment variables
If you’re using dotenv in code, just:
```
source .env  
```

# Run a test scripts
We’ve provided tests (or you can use the heredoc). To verify:
```
pytest
```

### Run the ETL test
```
python main.py
```
Expect output like:
```
Page 1 → 10 quotes
Page 2 → 10 quotes
Page 3 → 10 quotes
```
# Verify data landed in the quotes hypertable
In Adminer or via CLI:
```
docker-compose exec db psql -U <DB_USER> -d <DB_NAME> -c \
  "SELECT count(*) FROM quotes;"
```
You should see 30 (or however many) rows inserted.

# Cleanup (optional)
* To stop containers:
```
docker-compose down
```
* To wipe data (re‑init schema on next up):
```
docker-compose down -v
```