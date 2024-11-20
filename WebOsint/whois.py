from pprint import pprint
from ipwhois import IPWhois
from color import Color
import socket

def whois():
    def help():
        print(Color.CYAN + r"""
    : exit    Return to the main shell
                            """ + Color.RESET)
        return ""

    while True:
        input_user = input(Color.YELLOW + "Enter the Host Domain Name or 'exit' to quit > " + Color.RESET).strip()
        if input_user == "help" or input_user == "show options":
            help()
        elif input_user == "exit":
            return
        elif input_user == "":
            print(Color.RED + "[+] Please enter a domain name or 'exit' to quit." + Color.RESET)
        else:
            try:
                ip = socket.gethostbyname(input_user)
                ipwhois = IPWhois(ip)
                result = ipwhois.lookup_whois()
                print(Color.GREEN + "[+] Performing WHOIS lookup for " + input_user + Color.RESET)
                pprint(result)
            except Exception as e:
                print(Color.RED + "[+] An error occurred during WHOIS lookup:", e, Color.RESET)

if __name__ == "__main__":
    whois()
