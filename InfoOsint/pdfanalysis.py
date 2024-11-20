from PyPDF2 import PdfReader
import sys
from color import Color
import warnings

# Filter out PyPDF2 warnings
warnings.filterwarnings("ignore", category=UserWarning, module="PyPDF2")

def format_date(date_str):
    # Date format in PDF metadata: 'D:YYYYMMDDHHmmSS'
    return f"{date_str[6:8]}-{date_str[4:6]}-{date_str[2:4]} {date_str[8:10]}:{date_str[10:12]}:{date_str[12:14]}"

def pdfinfo():
    try:
        file_path = input(Color.YELLOW + "Enter PDF File path: " + Color.RESET)
        with open(file_path, 'rb') as f:
            pdf = PdfReader(f)
            info = pdf.metadata
            number_of_pages = len(pdf.pages)

            if info:
                print(Color.GREEN + "[+] PDF Information:")
                if info.get('/Author'):
                    print(Color.GREEN + "[+] Author        :", info.get('/Author'))
                
                if info.get('/Creator'):
                    print(Color.GREEN + "[+] Creator       :", info.get('/Creator'))
                
                if info.get('/Producer'):
                    print(Color.GREEN + "[+] Producer      :", info.get('/Producer'))
                
                if info.get('/Title'):
                    print(Color.GREEN + "[+] Title         :", info.get('/Title'))
                
                if info.get('/CreationDate'):
                    creation_date = format_date(info.get('/CreationDate'))
                    print(Color.GREEN + "[+] Creation Date :", creation_date)

                if info.get('/ModDate'):
                    modified_date = format_date(info.get('/ModDate'))
                    print(Color.CYAN + "[+] Modified Date :", modified_date)

                print(Color.CYAN + "[+] Number of Pages:", number_of_pages)
                
            else:
                print(Color.RED + "[-] No metadata available." + Color.RESET)

    except FileNotFoundError:
        print(Color.RED + "[-] File not found." + Color.RESET)
    
    except KeyboardInterrupt:
        print(Color.RED + "\nProgram Interrupted by user." + Color.RESET)
        sys.exit(1)

    except Exception as e:
        print(Color.RED + "[-] An error occurred:", str(e), Color.RESET)

if __name__ == "__main__":
    pdfinfo()
