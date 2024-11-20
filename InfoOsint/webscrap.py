import requests
from bs4 import BeautifulSoup
from color import Color

def Links():
    print(Color.YELLOW + "Note: http://example.com" + Color.RESET)
    url = input(Color.YELLOW + "Enter the URL: "+ Color.RESET)
    
    try:
        print('')
        print(Color.GREEN + "[+] Fetching links....." + Color.RESET)
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links_found = 0
            for link in soup.find_all('a'):
                lin = link.get('href')
                if lin and lin.startswith('http'):
                    print(Color.CYAN + "[+] ", lin)
                    links_found += 1
            if links_found == 0:
                print(Color.RED + "No links found on the webpage." + Color.RESET)
            else:
                print(Color.GREEN + "Fetched Successfully..." + Color.RESET)
        else:
            print(Color.RED + "[-] Failed to fetch the webpage." + Color.RESET)
            
    except requests.exceptions.RequestException as e:
        print(Color.RED + "[-] An error occurred:", str(e), Color.RESET)
    except KeyboardInterrupt:
        print(Color.RED + "\nOperation interrupted by the user."+ Color.RESET)

if __name__ == "__main__":
    Links()
