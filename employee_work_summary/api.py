import logging
import requests

class InvalidWorkLogError(Exception):
    pass

def is_public_holiday(date_str: str, country_code="AT") -> bool:
    try:
        year = date_str.split("-")[0]
        url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        holidays = response.json()
        for holiday in holidays:
            if holiday["date"] == date_str:
                return True
        return False

    except requests.exceptions.RequestException as e:
        logging.error(f"API error: {e}")
        raise InvalidWorkLogError("Failed to fetch public holidays")