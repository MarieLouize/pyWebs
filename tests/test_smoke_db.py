import os
import pandas as pd
import pytest
from sqlalchemy import create_engine, text
from datetime import datetime, timezone

@pytest.fixture(scope="module")
def engine():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise RuntimeError("Please export DATABASE_URL first")
    return create_engine(db_url)

@pytest.fixture(scope="module")
def cleanup_once(engine, request):
    def teardown():
        with engine.begin() as conn:
            conn.execute(
                text("DELETE FROM game_results WHERE home_team = 'X' AND away_team = 'Y'")
            )
    request.addfinalizer(teardown)

def test_insert_and_read_game_result(engine, cleanup_once):
    df = pd.DataFrame([{
        'game_date': '2025-05-07',
        'home_team': 'X',
        'away_team': 'Y',
        'home_score': 100,
        'away_score': 98,
        'scraped_at': datetime.now(timezone.utc)
    }])
    df.to_sql('game_results', engine, if_exists='append', index=False)

    result_df = pd.read_sql(
        "SELECT * FROM game_results ORDER BY scraped_at DESC LIMIT 1",
        engine
    )

    assert not result_df.empty
    assert result_df.iloc[0]['home_team'] == 'X'
    assert result_df.iloc[0]['away_team'] == 'Y'

def test_test_table_exists(engine):
    df = pd.read_sql("SELECT * FROM test_table", engine)
    assert not df.empty