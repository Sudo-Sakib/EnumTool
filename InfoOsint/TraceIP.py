import requests
from geopy.geocoders import Nominatim
from color import Color

def read_multiple_ip():
    try:
        ip_file = input(Color.YELLOW + "Enter the IP file path >> " + Color.RESET)

        with open(ip_file, "r") as f:
            for line in f:
                ip_address = line.strip()
                response = requests.get("http://ip-api.com/json/" + ip_address)
                data = response.json()

                if "lat" in data and "lon" in data:
                    print(Color.GREEN + f"IP location found for {ip_address}:" + Color.RESET)
                    print("Latitude: ", data["lat"])
                    print("Longitude: ", data["lon"])
                    print("Country: ", data.get("country", "Not Available"))
                    print("City: ", data.get("city", "Not Available"))
                    print("State: ", data.get("regionName", "Not Available"))
                    print("ZIP Code: ", data.get("zip", "Not Available"))
                    print("--------------------------------")
                else:
                    print(Color.RED + f"No location found for {ip_address}." + Color.RESET)

    except KeyboardInterrupt:
        print(Color.RED + "\nOperation interrupted by the user." + Color.RESET)

    except requests.ConnectionError:
        print(Color.RED + "Connection error. Please check your internet connection." + Color.RESET)

    except requests.Timeout:
        print(Color.RED + "Request timed out. Please try again later." + Color.RESET)

    except requests.RequestException as e:
        print(Color.RED + "An error occurred:", str(e), Color.RESET)

    except FileNotFoundError:
        print(Color.RED + "File not found. Please provide a valid file path." + Color.RESET)

if __name__ == "__main__":
    read_multiple_ip()
