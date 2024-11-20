import requests
from datetime import datetime
from color import Color

def urlinfo():
    print(Color.YELLOW + "Note: URL = http://example.com" + Color.RESET)
    url = input(Color.YELLOW + "Enter URL: " + Color.RESET)
    print(Color.GREEN + "-" * 50 + Color.RESET)
    print(Color.CYAN + "          Trace Results        ")
    print(Color.GREEN + "-" * 50 + Color.RESET)

    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        current_datetime = datetime.now()

        print()
        print(Color.GREEN + "[+] Traced Date and Time:", current_datetime, Color.RESET)
        print(Color.GREEN + "[+] Response Code:", response.status_code, Color.RESET)
        print(Color.GREEN + "[+] Final URL:", response.url, Color.RESET)

        if response.history:
            print(Color.GREEN + "[-] Redirection History:" + Color.RESET)
            for index, resp in enumerate(response.history, start=1):
                print(f"{index}. {resp.status_code} {resp.url}")

            print(Color.CYAN + "[-] Final Destination:", response.url, Color.RESET)
        else:
            print(Color.RED + "[-] No Redirections" + Color.RESET)

    except requests.exceptions.RequestException as e:
        print(Color.RED + "An error occurred:", str(e), Color.RESET)

    except KeyboardInterrupt:
        print(Color.RED + "\nOperation interrupted by the user." + Color.RESET)

if __name__ == "__main__":
    try:
        urlinfo()
    except Exception as e:
        print(Color.RED + "An error occurred: ", str(e), Color.RESET)
