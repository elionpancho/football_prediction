import mysql.connector
import logging
import handler
import schema

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    connection = None  # Initialize connection variable
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(user="root",
                                             password="P@ssw0rd",
                                             host="localhost",
                                             database="footballdb")
        if connection.is_connected():
            cursor = connection.cursor()
            logger.info("Database successfully connected")

            # Create tables
            schema.create_football_table(conn=connection, cursor=cursor)

            # Parameters for API request
            params = {"market": "classic", "iso_date": "2018-12-01", "federation": "UEFA"}

            # Insert football data
            football_data = handler.fetch_data('', params)  # Fetch data from API
            logger.debug(f"Fetched football data: {football_data}")  # Log the fetched data

            if isinstance(football_data, list):
                for football in football_data:
                    logger.debug(f"Processing football item: {football}")  # Log each item
                    flatten_dict = handler.flatten_football(football)  # Flatten each dictionary
                    schema.insert_into_football(data=flatten_dict, conn=connection, cursor=cursor)
            else:
                logger.error("Expected list of dictionaries, but got different structure")
        
    except mysql.connector.Error as err:
        logger.error(f"Error occurred while connecting to MySQL: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("MySQL connection closed")
