import requests
import logging
from exception import APIException
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

BASE_URL = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
API_KEY = "54840ff97cmsh32c90f471cf78d2p1779b1jsnd96faae30ef7"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "football-prediction-api.p.rapidapi.com"
}

def fetch_data(url_endpoint: str, params: dict) -> list:
    try:
        response = requests.get(f"{BASE_URL}/{url_endpoint}", headers=HEADERS, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        content = response.json()
        logger.debug(f"Fetched data: {content}")  # Log the fetched data
        return content['data'] if 'data' in content else []
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise APIException(code=response.status_code, message="Resource not found or unavailable") from http_err
    except requests.exceptions.RequestException as err:
        logger.error(f"Request error occurred: {err}")
        raise APIException(code=None, message="Request failed") from err

def flatten_football(football: dict) -> dict:
    try:
        start_date = datetime.fromisoformat(football['start_date'])
        last_update_at = datetime.fromisoformat(football['last_update_at'])
    except ValueError as e:
        logger.error(f"Error parsing dates: {e}")
        start_date = None
        last_update_at = None

    football_dict = {
        'home_team': football['home_team'],
        'away_team': football['away_team'],
        'id': football['id'],
        'market': football['market'],
        'competition_name': football['competition_name'],
        'prediction': football['prediction'],
        'competition_cluster': football['competition_cluster'],
        'status': football['status'],
        'federation': football['federation'],
        'is_expired': football['is_expired'],
        'season': football['season'],
        'result': football['result'],
        'start_date': start_date,
        'last_update_at': last_update_at,
        'odds_1': football['odds'].get('1'),
        'odds_2': football['odds'].get('2'),
        'odds_12': football['odds'].get('12'),
        'odds_X': football['odds'].get('X'),
        'odds_1X': football['odds'].get('1X'),
        'odds_X2': football['odds'].get('X2')
    }
    return football_dict
