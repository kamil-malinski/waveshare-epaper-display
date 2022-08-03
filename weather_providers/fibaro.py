import logging
from weather_providers.base_provider import BaseWeatherProvider
import requests

class Fibaro(BaseWeatherProvider):

    # Get data from Fibaro
    def get_weather(self):

        logging.info("GETTTING DATA FROM FIBARO")
        url = "http://eos.local/homestatus/get_value.php?"

        fibaro = {}

        response = requests.get(url + "id=352")
        response.raise_for_status()
        fibaro["temp_indoor_up"] = str(round(float(response.text),1))

        response = requests.get(url + "id=379")
        response.raise_for_status()
        fibaro["temp_indoor_down"] = str(round(float(response.text),1))

        response = requests.get(url + "id=401")
        response.raise_for_status()
        fibaro["temp_outdoor"] = str(round(float(response.text),1))

        logging.info(fibaro)
        logging.info("FIBARO ENDE")
        return fibaro
