import requests
import re

ip_info_url = "http://ipinfo.io/"

# use re to identify ip address and socket range in user input
ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# get ip address from user input
def get_ip_to_check():
    while True:
        ip = input("Please enter the IP address you would like to scan: ")
        m = re.search(ip_pattern, ip)
        if m:
            print(f"{m.group()} is a valid IP address.")
            return ip
        else:
            print(f"{ip} is not a valid ip address.")

def get_info(ip):

    # get the url to make the API call
    url = ip_info_url + ip + "/json"

    # store response from ipinfo.io
    response = requests.get(url)

    # convert json data into readable format in python
    data = response.json()

    # set in try as not all IPs are searchable
    try:
        # get geo-location data
        region = data['region']
        country = data['country']
        city = data['city']
        timezone = data['timezone']

        # output
        print(f"The entered IP address {ip} details is as follows:\nCountry: {country}\nRegion; {region}\nCity: {city}\nTimezone: {timezone}")
    except Exception:
        print("Either the IP address is invalid or the IP is secure.")

def main():
    get_info(get_ip_to_check())

if __name__ == "__main__":
    main()