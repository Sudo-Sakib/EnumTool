import os
from WebOsint.clickjack import ClickJacking
from WebOsint.hostheader import is_vulnerable_to_host_header_injection
from WebOsint.reverseip import reverse_ip_lookup
from WebOsint.subdomain import find_subdomains
from WebOsint.buildwith import analyze_website
from WebOsint.dns_enumeration import dnsrec
from WebOsint.web_crawl import perform_web_recon
from WebOsint.whois import whois
from color import Color

def set_color(text, color):
    return color + text + Color.RESET

def Webvuln():
    try:
        while True:
            inp = input(set_color("Vulnerability >> ", Color.YELLOW))

            if inp == '1':
                try:
                    print(set_color("Executing ClickJacking...", Color.CYAN))
                    ClickJacking()
                except KeyboardInterrupt:
                    print(set_color("\nProgram Interrupted: Exiting ClickJacking...", Color.RED))
                    break
                except Exception as e:
                    print(set_color("\nAn error occurred while fetching data:", str(e),Color.RED))
            
            elif inp == '2':
                try:
                    host_input = input(set_color("Enter Host Domain Name >> ", Color.YELLOW))
                    port_input = int(input(set_color("Enter Port Number >> ", Color.YELLOW)))
                    is_vulnerable_to_host_header_injection(host_input, port_input)
                except ValueError:
                    print(set_color("\nInvalid port input.", Color.RED))
                except Exception as e:
                    print(set_color("\nAn error occurred: " + str(e), Color.RED))
                except KeyboardInterrupt:
                    print(set_color("\nProgram Interrupted: Exiting Host Header Injection...", Color.RED))
                    
            
            elif inp == '3':
                try:
                    domain = input(Color.YELLOW + "Enter the domain name (e.g., youtube.com): "+Color.RESET)
                    filename = os.path.abspath("WebOsint\wordlist2.txt")
                    print(Color.CYAN+"Scanning for subdomains. Please wait..."+Color.RESET)
                    find_subdomains(domain, filename)
                except KeyboardInterrupt:
                    print(set_color("\nProgram Interrupted: Exiting SubDomain Enumeration...", Color.RED))
                except FileNotFoundError:
                    print(f"{Color.RED}[-] File not found: {filename}{Color.RESET}")
                except Exception as e:
                    print(f"[-]{Color.RED} An error occurred: {str(e)}{Color.RESET}")
                
            
            elif inp == '4':
                try:
                    reverse_input = input(set_color("Enter Host Domain Name >> ", Color.YELLOW))
                    reverse_ip_lookup(reverse_input)
                except Exception as e:
                    print(set_color("An error occurred: " + str(e), Color.RED))
                except KeyboardInterrupt:
                    print(set_color("\nProgram Interrupted: Exiting Reverse IP...", Color.RED))
                    
            
            elif inp == '5':
                try:
                    website_url = input(Color.YELLOW+"Enter the website URL: "+Color.RESET)
                    programming_languages, technologies, javascript_libraries, web_server = analyze_website(website_url)

                    if programming_languages:
                        print(Color.GREEN+"Detected programming languages:", ", ".join(programming_languages)+Color.RESET)
                    else:
                        print(Color.RED+"No programming language detected or an error occurred."+Color.RESET)

                    if technologies:
                        print(Color.CYAN + "\n Website technologies:")
                        for tech, details in technologies.items():
                            print(f"{tech}: {details}")
                        print(Color.RESET)
                    else:
                        print(Color.RED+"An error occurred while fetching technologies."+Color.RESET)

                    if javascript_libraries:
                        print(Color.CYAN+"\nJavaScript libraries:")
                        for library in javascript_libraries:
                            print("- " + library)
                        print(Color.RESET)
                    else:
                        print(Color.RED+"No JavaScript libraries detected."+Color.RESET)

                    print(Color.GREEN+"\nWeb server:", web_server,Color.RESET)
                
                except KeyboardInterrupt:
                    print(Color.RED+"\nProgram Iterrupted by user. Exiting Tehcnologies used in Website..."+Color.RESET)
                    
                except Exception as e:
                    return None, None, None, None, str(e)

            elif inp == '6':
                try:
                    target_domain = input(Color.YELLOW+"Enter the domain to perform DNS enumeration: "+Color.RESET)
                    result = dnsrec(target_domain)
                    print(result)
                except KeyboardInterrupt:
                    print(Color.RED+"\nProgram Iterrupted by user. Exiting DNS Enumeration..."+Color.RESET) 

            elif inp == '7':
                try:
                    target_website = input(Color.YELLOW+"Enter the URL (https://example.com): "+Color.RESET)
                    perform_web_recon(target_website)
                except KeyboardInterrupt:
                    print(Color.RED+"\nProgram Iterrupted by user. Exiting Web Crawl..."+Color.RESET)
            
            elif inp == '8':
                try:
                    whois()
                except KeyboardInterrupt:
                    print(Color.RED+"\nProgram Interrupted by user. Exiting WHOIS..."+Color.RESET)

            elif inp == 'tools':
                print(set_color("""
                                1. ClickJacking              
                                2. Host header injection     
                                3. Subdomain Enumeration     
                                4. Reverse IP
                                5. Website Analysis
                                6. DNS Enumeration
                                7. Web Crawl  
                                8. WHOIS             
                                """, Color.GREEN))
            
            elif inp == 'exit':
                print(set_color("Exiting Webvuln tool...", Color.GREEN))
                break
            
            else:
                print(set_color("Invalid choice", Color.RED))

    except KeyboardInterrupt:
        print(set_color("\nProgram Interrupted: Exiting WebVuln tool...", Color.RED))

if __name__ == "__main__":
    Webvuln()

