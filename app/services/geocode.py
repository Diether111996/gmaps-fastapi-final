import requests


def geocode_address(address: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json"
    }

    headers = {
        "User-Agent": "fastapi-maps-project"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if not data:
        return None

    return {
        "latitude": data[0]["lat"],
        "longitude": data[0]["lon"],
        "display_name": data[0]["display_name"]
    }