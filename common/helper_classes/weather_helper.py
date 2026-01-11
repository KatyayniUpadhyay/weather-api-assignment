import requests
import xml.etree.ElementTree as ET

from common.constants import Constants


class WeatherHelper:
    @staticmethod
    def fetch_weather(city):
        api_key = Constants.WEATHER_API_KEY

        if not api_key:
            raise Exception("API key not configured")

        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        }

        params = {"q": city}

        response = requests.get(
            Constants.WEATHER_API_URL,
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        print(response.status_code)
        print(response.text)

        data = response.json()

        if "error" in data:
            raise Exception(data["error"]["message"])

        return data

    @staticmethod
    def extract_weather_data(data):
        current = data.get("current", {})
        location = data.get("location", {})

        return {
            "temperature": current.get("temp_c", "NA"),
            "latitude": location.get("lat", "NA"),
            "longitude": location.get("lon", "NA"),
            "city": f'{location.get("name", "")} {location.get("country", "")}'.strip(),
        }

    @staticmethod
    def build_json_response(weather_data):
        return {
            "Weather": f'{weather_data["temperature"]} C',
            "Latitude": str(weather_data["latitude"]),
            "Longitude": str(weather_data["longitude"]),
            "City": weather_data["city"],
        }

    @staticmethod
    def build_xml_response(weather_data):
        root = ET.Element("root")

        ET.SubElement(root, "Temperature").text = str(
            weather_data["temperature"]
        )
        ET.SubElement(root, "City").text = weather_data["city"]
        ET.SubElement(root, "Latitude").text = str(
            weather_data["latitude"]
        )
        ET.SubElement(root, "Longitude").text = str(
            weather_data["longitude"]
        )

        return ET.tostring(
            root,
            encoding="utf-8",
            xml_declaration=True,
        )
