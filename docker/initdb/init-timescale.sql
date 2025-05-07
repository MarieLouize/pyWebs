-- Ensure the TimescaleDB extension is available
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create the quotes table if missing
CREATE TABLE IF NOT EXISTS quotes (
  page        INT,
  quote       TEXT,
  author      TEXT,
  tags        TEXT,
  scraped_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Turn it into a hypertable (if_not_exists flag is supported in TS>=2.3)
SELECT create_hypertable(
  'quotes',           -- table name
  'scraped_at',       -- time column
  if_not_exists => TRUE
);
