# EnumTool
Enumeration Tool encompasses multiple modules related to information gathering, web vulnerability assessment, each module has different algorithms or techniques used depending on its specific purpose.

A. Information Gathering:

![Screenshot 2024-11-20 141106](https://github.com/user-attachments/assets/7d41f77a-1055-4ef2-a4db-c798ec181f0a)

 1. Phone Number Verifier:
    Validates the phone number and Retrieves timezone, carrier, location, number possibility, formatted number, and number type information.
 
 2. Single IP Locator:
    Extracts and displays information about the IP address's location, including country, region, city, timezone, ISP, latitude, and longitude. It also opens a web browser and displays the location on Google Maps.
 
 3. Multiple IP Address Locator:
    Displays the geolocation details including latitude, longitude, country, city, state, and ZIP code.
 
 4. PDF Analysis:
    Extract and display metadata information such as author, creator, producer, title, creation date, and modified date (if available). Also, display the number of pages in the PDF.
 
 6. URL Lookup in web pages:
    Attempt to fetch the webpage using an HTTP GET request.
    
 7. URL Redirection:
    Capture the response, its status code, and the final URL (including any redirects).
 
 8. Wayback Enumeration:
    Checks if a given target URL is available in the Wayback Machine archive.

 9. Username Checker:
 Searches for a given username across multiple websites by constructing URLs for various social media and online platforms. It then checks if the username is present on those websites by sending HTTP requests and analyzing the responses.
 
B. WebVulnerability:

![image](https://github.com/user-attachments/assets/50180c7b-2f7f-4f0f-b5b7-9796722aa532)

 1. Clickjacking:
Check the response headers to see if the "X-Frame-Options" header is present. If the header is missing, it suggests the website is vulnerable to ClickJacking and displays a message.
 
 2. Host Header Injection:
    Check for the host header injection vulnerability.

 4. SubDomain Enumeration:
    Prints the total number of subdomains scanned, subdomains found, and the elapsed time. It then displays the links of the subdomains found.
 
 5. Reverse IP
    This Python script performs a reverse IP lookup using the HackerTarget API to find domains associated with a given IP address.
    
 6. Technologies used in website:
    Detects programming languages used in the website's content. Using the builtwith library to retrieve website technologies.
   
 7. DNS Enumeration:
    Queries various DNS record types (A, AAAA, CAA, CNAME, MX, NS, TXT) for the domain. Queries the DMARC record for the domain, if available.
   
 8. Web Crawl:
    Extracts and prints URLs of various types of files (JS, CSS, HTML, PHP, images), internal links, and external links found on the website.
    
 9. WHOIS:
    The WHOIS information for the IP address is retrieved and displayed, providing details about the registered owner, organization, and other relevant                 information.

****Installation*****
 git clone https://github.com/Sudo-Sakib/EnumTool.git
 cd EnumTool/
 pip install -r requirements.txt

****Run*****
python3 EnumTool.py

