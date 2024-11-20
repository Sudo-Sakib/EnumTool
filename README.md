# EnumTool
Enumeration Tool encompasses multiple modules related to information gathering, web vulnerability assessment, each module has different algorithms or techniques used depending on its specific purpose.

A. Information Gathering:

**Screenshot**
![Screenshot 2024-11-20 141106](https://github.com/user-attachments/assets/7d41f77a-1055-4ef2-a4db-c798ec181f0a)


 1. Phone Number Verifier:
   ● User enters a phone number with a country code.
   ● It validates if the number is valid.
   ● Retrieves and displays timezone, carrier, location, number possibility, formatted number, and number type information.
 
 2. Single IP Locator:
   ● User inputs an IP address.
   ● The script constructs an API URL with the provided IP address.
   ● It sends an HTTP request to the API and receives a JSON response.
   ● If the API response status is "success," it extracts and displays information about the IP address's location, including country, region, city, timezone,          ISP, latitude, and longitude.
   ● It also opens a web browser and displays the location on Google Maps.
 
 3. Multiple IP Address Locator:
   ● User inputs the path to a file containing a list of IP addresses.
   ● The script reads each IP address from the file, one by one.
   ● It sends an HTTP request to the "ip-api.com" API for each IP address to retrieve geolocation data.
   ● If the API response contains latitude and longitude information, it displays the geolocation details including latitude, longitude, country, city, state, and      ZIP code.
   ● If the API response does not contain location information, it indicates that no location was found for that IP address.
 
 4. PDF Analysis:
   ● Prompt the user for a PDF file path. Extract and display metadata information such as author, creator, producer, title, creation date, and modified date (if available). Also, display the number of pages in the PDF.
 
 6. URL Lookup in web pages:
   ● Promptthe user to input a URL.
   ● Attempt to fetch the webpage using an HTTP GET request.
   ● If successful, parse the webpage's HTML and extract and display all links starting with 'http'.
 
 7. URL Redirection:
   ● Prompt the user to enter a URL and capture it.Capture the response, its status code, and the final URL (including any redirects).
 
 8. Wayback Enumeration:
   ● Define a function check_wayback_availability(target): This function checks if a given target URL is available in the Wayback Machine archive.

 9. Username Checker:
 ● Searches for a given username across multiple websites by constructing URLs for various social media and online platforms. It then checks if the username is       present on those websites by sending HTTP requests and analyzing the responses.
 
B. WebVulnerability:

**Screenshot**

![image](https://github.com/user-attachments/assets/50180c7b-2f7f-4f0f-b5b7-9796722aa532)

 1. Clickjacking:
   ● Prompt the user to input a host domain name and port number. Validate the port input. Construct a URL using the provided host and port.
   ● Attempt to fetch data from the URL: Check the response headers to see if the "X-Frame-Options" header is present. If the header is missing, it suggests the       website is vulnerable to ClickJacking and displays a message.
 
 2. Host Header Injection:
   ● This Python script checks if a website is vulnerable to Host Header Injection, a security vulnerability.
   ● The user inputs a host domain name and port number.
   ● The script constructs a URL with the provided host and port.
   ● It sends an HTTP GETrequest to that URL with a modified 'Host' header.
   ● If the response headers contain 'evil.com,' it's considered vulnerable to Host Header Injection; otherwise, it's not.
 
 3. SubDomain Enumeration:
   ● This Python script performs a subdomain enumeration for a given domain using multithreading.
   ● The user provides a domain name.
   ● The script reads a list of subdomains from a file named "wordlist2.txt."
   ● It spawns multiple threads to check the existence of subdomains by making HTTP requests to subdomain URLs.
   ● If a subdomain exists (returns HTTP status 200), it's added to a list of subdomains found.
   ● After all threads finish execution, the script prints the total number of subdomains scanned, subdomains found, and the elapsed time.
   ● It then displays the links of the subdomains found.
 
 4. Reverse IP
   ● This Python script performs a reverse IP lookup using the HackerTarget API to find domains associated with a given IP address.
   ● The user provides a host (IP address or domain name).
   ● The script constructs a URL for the reverse IP lookup using the HackerTarget API.
   ● It sends an HTTP GETrequest to that URL.
   ● If the response status code is 200, it prints the results, which are the domains associated with the provided IP address.
   ● Ifthe response status code is not 200, it indicates that the reverse IP lookup failed.
 
 5. Technologies used in website:
   ● Detects programming languages used in the website's content.
   ● Using the builtwith library to retrieve website technologies.
   ● Parse the HTML content to extract JavaScript libraries.
   ● Gets web server information from the response headers.
 
 6. DNS Enumeration:
   ● This Python script performs DNS enumeration for a given domain.
   ● Setup a DNSresolver with a timeout.
   ● Queries various DNS record types (A, AAAA, CAA, CNAME, MX, NS, TXT) for the domain.
   ● Queries the DMARC record for the domain, if available.
   ● Prints the results, including DNS records and DMARC records.
 
 7. Web Crawl:
   ● This Python script performs web reconnaissance on a given website.
   ● Sends a GETrequest to the website and retrieves its HTML content.
   ● Parses the HTML content using BeautifulSoup.
   ● Extracts and prints URLs of various types of files (JS, CSS, HTML, PHP, images), internal links, and external links found on the website.
   ● Optionally, it searches for and prints links from a specific directory on the website.
   ● Displays counts of different types of files and links.
 
 8. WHOIS:
   ● This Python script performs a WHOIS lookup for a given host domain name.
   ● It provides a command-line interface for the user to input a host domain name.
   ● If the user enters "exit," the script exits. If they enter "help" or "show options," it displays help information.
   ● If the user enters a valid host domain name (not empty), it attempts to resolve the IP address associated with that domain using the socket.gethostbyname           function.
   ● It then uses the IPWHOIS library to perform a WHOIS lookup on the IP address.
   ● The WHOIS information for the IP address is retrieved and displayed, providing details about the registered owner, organization, and other relevant                 information.

**Installation**
git clone https://github.com/Sudo-Sakib/EnumTool.git
cd EnumTool/
pip install -r requirements.txt

**Run**
python3 EnumTool.py

