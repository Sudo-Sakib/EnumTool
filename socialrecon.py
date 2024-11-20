from color import Color
from InfoOsint.number import number            
from InfoOsint.iplocator import iplocate         
from InfoOsint.TraceIP import read_multiple_ip  
from InfoOsint.pdfanalysis import pdfinfo       
from InfoOsint.webscrap import Links            
from InfoOsint.url import urlinfo 
from InfoOsint.wayback import fetch_wayback_links
from InfoOsint.social_media import search

def reconinput():
    print(Color.GREEN + "Welcome to OSINT Information Gathering Tool\n" + Color.RESET)
    
    while True:
        try:
            inp = input(Color.YELLOW + "Information Gathering >> " + Color.RESET)

            if inp == '1':
                try:
                    number()
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting Phone Number Verifier..." + Color.RESET)
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) + Color.RESET) 

            elif inp == '2':             
                try:
                    iplocate()
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting IP Locator..." + Color.RESET)
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) + Color.RESET)

            elif inp == '3':
                try:
                    read_multiple_ip()
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting Multiple IP Locator..." + Color.RESET)
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) + Color.RESET)

            elif inp == '4':
                try:
                    pdfinfo()
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting Meta Data Extractor..." + Color.RESET)
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) + Color.RESET)

            elif inp == '5':
                try:
                    Links()
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. URL Lookup..." + Color.RESET)
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) + Color.RESET)

            elif inp == '6':
                try:
                    urlinfo()
                except Exception as e:
                    print(Color.RED + "\nAn error occurred: ", str(e) +Color.RESET)
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting URL Redirection..." + Color.RESET)
            
            elif inp == '7':
                try:
                    target= input(Color.YELLOW + "Enter the domain name (example.com): " + Color.RESET)
                    fetch_wayback_links(target)
                except Exception as e:
                    print(Color.RED + f"[-] An error occurred: {str(e)}"+ Color.RESET)
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted by user. Exiting WayBack Enumeration..."+ Color.RESET)
            
            elif inp == '8':
                try:
                    username = input("Enter Username >> ")
                    search(username)
                except KeyboardInterrupt:
                    print(Color.RED + "\nProgram Interrupted: Exiting Username Checker...")
                except Exception as e:
                    print(Color.RED + "An error occurred: " + str(e), Color.RESET)
                   
        
            elif inp.lower() == 'exit':
                print(Color.RED + "\nExiting Information Gathering..." + Color.RESET)
                return
    
            elif inp.lower() == 'tools':

                print(Color.GREEN + """Tools available 
                    1. Phone Number Verifier              
                    2. Trace Single IP                   
                    3. Multiple IP Locator               
                    4. PDF meta data analysis            
                    5. URL lookup in webpages            
                    6. URL redirection checker           
                    7. WayBack Enumeration
                    8. Username Checker
                    usage: type exit to stop
                """ + Color.RESET)
        
            else:
                print(Color.RED + "Enter a valid option" + Color.RESET)
        
        except KeyboardInterrupt:
            print(Color.RED + "\nProgram interrupted by user." + Color.RESET)
            break
            
        except Exception as e:
            print(Color.RED + f"An error occurred: {e}" + Color.RESET)
            break

if __name__ == "__main__":
    reconinput()
    