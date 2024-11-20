import requests
from color import Color

def reverse_ip_lookup(host):
    try:
        lookup = f'<HACKER TARGET API KEY>={host}'
        response = requests.get(lookup)
        
        if response.status_code == 200:
            result = response.text
            print(Color.CYAN + "[+]" + result + Color.RESET)
        else:
            print(Color.RED + "Reverse IP lookup failed. API returned:", response.status_code,Color.RESET)

    except requests.exceptions.RequestException as e:
        print(Color.RED + "An error occurred:", e,Color.RESET)
    except KeyboardInterrupt:
        print(Color.RED+"\nKeyboardInterrupt: Exiting Reverse IP Lookup..."+Color.RESET)
    except Exception as ex:
        print(Color.RED + "An unexpected error occurred:", str(ex),Color.RESET)

if __name__ == "__main__":
    try:
        host_input = input(Color.YELLOW+"Enter Host Domain Name >> "+Color.RESET)
        reverse_ip_lookup(host_input)
    except KeyboardInterrupt:
        print(Color.RED+"\nKeyboardInterrupt: Exiting Reverse IP Lookup..."+Color.RESET)
    
    except Exception as e:
        print(Color.RED + "An unexpected error occurred:", str(e),Color.RESET)
        
