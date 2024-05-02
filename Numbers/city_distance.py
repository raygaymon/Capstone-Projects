import requests
from geopy import distance
# get lat and lon from weatherapi

API_KEY = "577269b266d2486cdd18779b8517aa7c"

BASE_URL = "http://api.openweathermap.org/geo/1.0/direct?"

def get_lat_lon(n):

    city = input(f"Enter City {n}: ")
    request_url = f"{BASE_URL}q={city}&appid={API_KEY}"
    response_1 = requests.get(request_url)

    # check for successful response 200
    if response_1.status_code == 200:
        data = response_1.json()
        lat = data[0]['lat']
        lon = data[0]['lon']
        return (lat, lon)
    else:
        print("Something went wrong.")

def main():

    city_1 = get_lat_lon(1)
    city_2 = get_lat_lon(2)
    print(f"Distance between the 2 cities is {round(distance.geodesic(city_1, city_2).kilometers, 2)}km.")

main()




