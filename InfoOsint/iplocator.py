import requests
import webbrowser
from color import Color

def iplocate():
    try:
        ip = input(Color.YELLOW + "Enter the IP address: " + Color.RESET)

        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        ipinfo = response.json()

        if ipinfo['status'] == 'success':
            lat = ipinfo['lat']
            lon = ipinfo['lon']
            print(Color.GREEN + "IP location found:")
            print('Country     :', ipinfo['country'])
            print('Country Code:', ipinfo['countryCode'])
            print('Region Name :', ipinfo['regionName'])
            print('Region      :', ipinfo['region'])
            print('City        :', ipinfo['city'])
            print('ZIP Code    :', ipinfo['zip'])
            print('Time zone   :', ipinfo['timezone'])
            print('ISP         :', ipinfo['isp'])
            print('Latitude    :', lat)
            print('Longitude   :', lon)
            print(Color.CYAN + 'Opening location in browser...')
            mapurl = f"https://maps.google.com/maps?q={lat},{lon}"
            webbrowser.open(mapurl, new=2)
            print('')
        else:
            print(Color.RED + "IP location not found.")

    except KeyboardInterrupt:
        print(Color.RED + "Operation interrupted by the user. Exiting IP Locator..." + Color.RESET)
    
    except requests.ConnectionError:
        print(Color.RED + "Connection error. Please check your internet connection.")
    
    except requests.Timeout:
        print(Color.RED + "Request timed out. Please try again later.")
    
    except requests.RequestException as e:
        print(Color.RED + "An error occurred:", str(e))

if __name__ == "__main__":
    iplocate()
