import requests
from colorama import init, Fore
import threading
import time
import os
from color import Color

init()

def find_subdomains(domain, filename, timeout=20):
    subdomains_found = []
    subdomains_lock = threading.Lock()

    def check_subdomain(subdomain):
        subdomain_url = f"https://{subdomain}.{domain}"

        try:
            response = requests.get(subdomain_url, timeout=timeout)
            if response.status_code == 200:
                with subdomains_lock:
                    subdomains_found.append(subdomain_url)
                    print(f"{Color.GREEN}Subdomain Found [+]: {subdomain_url}{Color.RESET}")
        except requests.exceptions.RequestException as e:
            if "Max retries exceeded with url" in str(e):
                pass
            else:
                print(f"{Color.RED}[-] Error checking subdomain {subdomain_url}: {str(e)}{Color.RESET}")

    try:
        with open(filename, "r") as file:
            subdomains = [line.strip() for line in file.readlines()]

        print(f"{Color.CYAN}Starting threads...")
        start_time = time.time()

        threads = []
        for subdomain in subdomains:
            thread = threading.Thread(target=check_subdomain, args=(subdomain,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{Color.GREEN}[+] {Color.CYAN}Total Subdomains Scanned:{Color.RESET} {len(subdomains)}")
        print(f"{Color.GREEN}[+] {Color.CYAN}Total Subdomains Found:{Color.RESET} {len(subdomains_found)}")
        print(f"{Color.GREEN}[+] {Color.CYAN}Time taken:{Color.RESET} {elapsed_time:.2f} seconds")
        print(Color.GREEN + "\nSubdomains Found Links:" + Color.RESET)
        for link in subdomains_found:
            print(link)

    except FileNotFoundError:
        print(f"{Color.RED}[-] File not found: {filename}{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}[-] An error occurred: {str(e)}{Color.RESET}")

if __name__ == "__main__":
    try:
        domain = input(Color.YELLOW + "Enter Domain Name >> " + Color.RESET)
        filename = os.path.abspath("WebOsint\wordlist2.txt")
        print(f"{Color.GREEN}Scanning for subdomains. Please wait...{Color.RESET}")
        find_subdomains(domain, filename)
    except KeyboardInterrupt:
        print(f"{Color.RED}[-] Program Interrupted by user.{Color.RESET}")
