import logging
import mysql.connector

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_football_table(conn, cursor):
    try:
        query = """
                CREATE TABLE IF NOT EXISTS football(
                    home_team VARCHAR(225),
                    away_team VARCHAR(225),
                    id INT PRIMARY KEY,
                    market VARCHAR(255),
                    competition_name VARCHAR(255),
                    prediction VARCHAR(255),
                    competition_cluster VARCHAR(255),
                    status VARCHAR(255),
                    federation VARCHAR(255),
                    is_expired BOOLEAN,
                    season VARCHAR(255),
                    result VARCHAR(255),
                    start_date DATETIME,
                    last_update_at DATETIME,
                    odds_1 FLOAT,
                    odds_2 FLOAT,
                    odds_12 FLOAT,
                    odds_X FLOAT,
                    odds_1X FLOAT,
                    odds_X2 FLOAT
                );
        """
        cursor.execute(query)
        conn.commit()
        logger.info("Table 'football' was successfully created")
    except mysql.connector.Error as err:
        logger.error(f"An error occurred while creating the table: {err}")

def insert_into_football(data, conn, cursor):
    try:
        query = """
                INSERT INTO football(home_team, away_team, id, market, competition_name, prediction, competition_cluster, status, federation, is_expired, season, result, start_date, last_update_at, odds_1, odds_2, odds_12, odds_X, odds_1X, odds_X2)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            data['home_team'], data['away_team'], data['id'], data['market'], data['competition_name'],
            data['prediction'], data['competition_cluster'], data['status'], data['federation'], data['is_expired'],
            data['season'], data['result'], data['start_date'], data['last_update_at'], data['odds_1'],
            data['odds_2'], data['odds_12'], data['odds_X'], data['odds_1X'], data['odds_X2']
        )
        cursor.execute(query, values)
        conn.commit()
        logger.info("Data inserted into table 'football' successfully")
    except mysql.connector.Error as err:
        logger.error(f"An error occurred while inserting into the table: {err}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
