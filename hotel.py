import http.client
import json

def search_hotels(hotel_id):
    conn = http.client.HTTPSConnection("hotels-com-provider.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "00c2984462mshe7ca93b291d94a5p1620d4jsn8e6c5313d0f3",
        'X-RapidAPI-Host': "hotels-com-provider.p.rapidapi.com"
    }
    endpoint = f"/v2/hotels/summary?hotel_id={hotel_id}&locale=en_GB&domain=AE"
    conn.request("GET", endpoint, headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def parse_hotels_data(data):
    try:
        data = json.loads(data)
        property_info = data.get('summary')
        if property_info:
            hotel_name = property_info.get('name')
            tagline = property_info.get('tagline')
            if hotel_name:
                return hotel_name, tagline
        return None, None
    except Exception as e:
        print(f"Error parsing hotels data: {e}")
        return None, None