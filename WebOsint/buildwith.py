import requests
import builtwith
from bs4 import BeautifulSoup
import re
from color import Color

def analyze_website(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        html_content = response.text

        # Detect programming languages
        programming_languages = detect_programming_language(html_content)

        # Use builtwith library to get website details
        technologies = builtwith.builtwith(url)

        # Parse HTML to extract JavaScript libraries
        javascript_libraries = extract_javascript_libraries(html_content)

        # Get web server information from response headers
        web_server = response.headers.get("Server", "Unknown")

        return programming_languages, technologies, javascript_libraries, web_server
    
    except requests.Timeout:
        return None, None, None, None, "Request timed out"
    
    except requests.RequestException as e:
        return None, None, None, str(e)
    
    except Exception as e:
        return None, None, None, None, str(e)

def detect_programming_language(content):
    # Define patterns for various programming languages
    patterns = {
        "PHP": r"<\?php|\.php",
        "Python": r"python",
        "Ruby": r"ruby",
        "Java": r"\bjava\b",
        "JavaScript": r"javascript",
        "ASP.NET": r"asp\.net",
    }

    detected_languages = []

    for language, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            detected_languages.append(language)

    return detected_languages


def extract_javascript_libraries(content):
    soup = BeautifulSoup(content, "html.parser")
    script_tags = soup.find_all("script")

    libraries = set()

    for script in script_tags:
        src = script.get("src")
        if src:
            match = re.search(r"/(.*?)(?:\.min)?\.js$", src)
            if match:
                libraries.add(match.group(1))

    return list(libraries)


if __name__ == "__main__":

    website_url = input(Color.YELLOW+"Enter the website URL: "+Color.RESET)
    programming_languages, technologies, javascript_libraries, web_server = analyze_website(website_url)

    if programming_languages:
        print(Color.GREEN + "Detected programming languages:", ", ".join(programming_languages) + Color.RESET)
    else:
        print(Color.RED + "No programming language detected or an error occurred." + Color.RESET)

    if technologies:
        print("\n" + Color.CYAN + "Website technologies:")
        for tech, details in technologies.items():
            print(f"{tech}: {details}")
        print(Color.RESET)
    else:
        print(Color.RED+"An error occurred while fetching technologies." + Color.RESET)

    if javascript_libraries:
        print("\n"+ Color.YELLOW + "JavaScript libraries:" + Color.RESET)
        for library in javascript_libraries:
            print("- " + library)
        print(Color.RESET)
    else:
        print(Color.RED + "No JavaScript libraries detected." + Color.RESET)

    print("\nWeb server:", web_server)