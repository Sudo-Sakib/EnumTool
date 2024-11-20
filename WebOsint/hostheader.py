import requests
import sys
from color import Color

def is_vulnerable_to_host_header_injection(host, port):
    try:
        if port == 80:
            scheme = 'http://'
        elif port == 443:
            scheme = 'https://'
        else:
            print(Color.RED + "Couldn't fetch data for the given PORT" + Color.RESET)
            return

        url = scheme + host
        headers = {'Host': 'http://evil.com'}

        response = requests.get(url, headers=headers)
        if 'evil.com' in response.headers:
            print(Color.GREEN + "Vulnerable to Host Header Injection"+ Color.RESET)
        else:
            print(Color.RED + "Not Vulnerable to Host Header Injection"+ Color.RESET)

    except requests.exceptions.RequestException as e:
        print(Color.RED + "An error occurred:", e, Color.RESET)
    
    except KeyboardInterrupt:
        print(Color.RED + "\nKeyboardInterrupt: Exiting Host Header Injection checker..."+ Color.RESET)
            

if __name__ == "__main__":
    try:
        host_input = input(Color.YELLOW + "Enter Host Domain Name >> "+ Color.RESET)
        port_input = input(Color.YELLOW + "Enter Port Number>> "+ Color.RESET)
        
        if not port_input.isdigit():
            print(Color.RED + "Invalid port input. Please enter a valid integer."+ Color.RESET)
            
            
        port = int(port_input)
        is_vulnerable_to_host_header_injection(host_input, port)

    except KeyboardInterrupt:
        print(Color.RED + "\nKeyboardInterrupt: Exiting Host Header Injection checker..."+ Color.RESET)
          
    except ValueError:
        print(Color.RED + "Invalid port input. Please enter a valid integer."+ Color.RESET)
        
