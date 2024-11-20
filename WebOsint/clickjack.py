from urllib.request import urlopen
from color import Color

def ClickJacking():
    try:
        host = input(Color.YELLOW + "Enter Host Domain Name>> "+ Color.RESET)
        port = input(Color.YELLOW + "Enter Port Number >> "+ Color.RESET)

        if not port.isdigit():
            print(Color.RED + "Invalid port input. Please enter a valid integer." + Color.RESET)
            return

        port = int(port)
        if port == 80:
            port = 'http://'
        elif port == 443:
            port = 'https://'
        else:
            print(Color.RED + "Couldn't fetch data for the given PORT"+ Color.RESET)
            return

        url = port + host

        try:
            data = urlopen(url)
            headers = data.info()

            if not "X-Frame-Options" in headers:
                print(Color.GREEN + "Website is vulnerable to ClickJacking"+ Color.RESET)
            else:
                print(Color.RED + "Website is not Vulnerable to ClickJacking"+ Color.RESET)
        
        except Exception as e:
            print(Color.RED + "An error occurred while fetching data:", str(e),+ Color.RESET)
    
    except KeyboardInterrupt:
        print(Color.RED + "\nKeyboardInterrupt: Exiting ClickJacking checker..."+ Color.RESET)
        

if __name__ == "__main__":
    ClickJacking()
