import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin
import sys
from color import Color

def perform_web_recon(website_url):
    # Set timeout values in seconds
    timeout = 10

    try:
        # Send a GET request to the website
        response = requests.get(website_url, timeout=timeout)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Lists to store URLs of different types of files
            js_files = []
            css_files = []
            html_files = []
            php_files = []
            image_files = []
            internal_links = set()
            external_links = set()

            # Regular expression pattern to match file extensions
            file_extension_pattern = r'\.([a-zA-Z0-9]+)$'

            # Find all <script> tags and extract src URLs
            for script_tag in soup.find_all('script', src=True):
                src = script_tag['src']
                js_files.append(src)

            # Find all <link> tags with rel="stylesheet" and extract href URLs
            for link_tag in soup.find_all('link', rel='stylesheet', href=True):
                href = link_tag['href']
                css_files.append(href)

            # Find all <a> tags and extract href URLs
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if re.search(file_extension_pattern, href):
                    extension = re.search(file_extension_pattern, href).group(1)
                    if extension == 'html':
                        html_files.append(href)
                    elif extension == 'php':
                        php_files.append(href)
                    else:
                        image_files.append(href)
                else:
                    if href.startswith('#'):
                        continue
                    full_url = urljoin(website_url, href)
                    parsed_url = urlparse(full_url)
                    if parsed_url.netloc == urlparse(website_url).netloc:
                        internal_links.add(full_url)
                    else:
                        external_links.add(full_url)

            # Print the URLs
            print(f"{Color.GREEN}[+] JS Files:{Color.RESET}")
            for js_file in js_files:
                print(js_file)

            print(f"\n{Color.GREEN}[+] CSS Files:{Color.RESET}")
            for css_file in css_files:
                print(css_file)

            print(f"\n{Color.GREEN}[+] HTML Files:{Color.RESET}")
            for html_file in html_files:
                print(html_file)

            print(f"\n{Color.GREEN}[+] PHP Files:{Color.RESET}")
            for php_file in php_files:
                print(php_file)

            print(f"\n{Color.GREEN}[+] Image Files:{Color.RESET}")
            for image_file in image_files:
                print(image_file)

            print(f"\n{Color.GREEN}[+] Internal Links:{Color.RESET}")
            for internal_link in internal_links:
                print(internal_link)

            print(f"\n{Color.GREEN}[+] External Links:{Color.RESET}")
            for external_link in external_links:
                print(external_link)

            # Directory search and print details
            directory_search = website_url + "/directory"  # Replace with the directory you want to search
            directory_response = requests.get(directory_search, timeout=timeout)

            if directory_response.status_code == 200:
                directory_soup = BeautifulSoup(directory_response.content, 'html.parser')
                directory_links = []

                # Find all <a> tags in the directory page
                for a_tag in directory_soup.find_all('a', href=True):
                    href = a_tag['href']
                    full_url = urljoin(directory_search, href)
                    directory_links.append(full_url)

                print("\nDirectory Links:")
                for directory_link in directory_links:
                    print(directory_link)

            else:
                print(f"{Color.RED}Failed to fetch directory. Status code:", directory_response.status_code,Color.RESET)

            # Print the counts
            print(f"\n{Color.GREEN}[+] Total JS Files:{Color.RESET}", len(js_files))
            print(f"{Color.GREEN}[+] Total CSS Files:{Color.RESET}", len(css_files))
            print(f"{Color.GREEN}[+] Total HTML Files:{Color.RESET}", len(html_files))
            print(f"{Color.GREEN}[+] Total PHP Files:{Color.RESET}", len(php_files))
            print(f"{Color.GREEN}[+] Total Image Files:{Color.RESET}", len(image_files))
            print(f"{Color.GREEN}[+] Total Internal Links:{Color.RESET}", len(internal_links))
            print(f"{Color.GREEN}[+] Total External Links:{Color.RESET}", len(external_links))

        else:
            print(f"{Color.RED}Failed to fetch the website. Status code:", response.status_code,Color.RESET)

    except requests.Timeout:
        print(f"{Color.RED}Request timed out.{Color.RESET}")
    except requests.RequestException as e:
        print(f"{Color.RED}An error occurred: {str(e)}{Color.RESET}")
    except KeyboardInterrupt:
        print(f"{Color.RED}\nKeyboard interruption detected. Exiting...{Color.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    target_website = input(f"{Color.YELLOW}Enter the URL (https://example.com{Color.RESET}): ")
    perform_web_recon(target_website)
