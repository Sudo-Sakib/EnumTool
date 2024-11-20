import requests
from datetime import date
from color import Color


WAYBACK_AVAIL_URL = 'http://archive.org/wayback/available'
WAYBACK_SEARCH_URL = 'http://web.archive.org/cdx/search/cdx'


def print_status(status, color, message):
    print(f'{Color.YELLOW}[!] {Color.CYAN}{message}', end='', flush=True)
    print(f'{color}[' + '.'.rjust(5, '.') + f' {status} ]{Color.RESET}')


def check_wayback_availability(target):
    avail_data = {'url': target}

    try:
        check_rqst = requests.get(WAYBACK_AVAIL_URL, params=avail_data, timeout=10)
        check_sc = check_rqst.status_code
        if check_sc == 200:
            check_data = check_rqst.json()
            if check_data['archived_snapshots']:
                print_status('Available', Color.GREEN, 'Checking Availability on Wayback Machine')
                return True
            else:
                print_status('N/A', Color.RED, 'Checking Availability on Wayback Machine')
        else:
            print(f'\n{Color.RED}[-] Status : {Color.CYAN}{check_sc}{Color.RESET}')
    except requests.exceptions.RequestException as e:
        print(f'\n{Color.RED}[-] Exception : {Color.CYAN}{e}{Color.RESET}')
    except Exception as e:
        print(f'\n{Color.RED}[-] Exception : {Color.CYAN}{e}{Color.RESET}')

    return False


def fetch_wayback_links(target):
    if not check_wayback_availability(target):
        return

    print_status('Fetching URLs', Color.CYAN, 'Fetching URLs')

    curr_yr = date.today().year
    last_yr = curr_yr - 5

    payload = {
        'url': f'{target}/*',
        'fl': 'original',
        'fastLatest': 'true',
        'from': str(last_yr),
        'to': str(curr_yr)
    }

    try:
        r = requests.get(WAYBACK_SEARCH_URL, params=payload)
        r_sc = r.status_code
        if r_sc == 200:
            r_data = set(r.text.split('\n'))
            print_status(len(r_data), Color.GREEN, f'Fetching URLs')
            result = {'links': list(r_data), 'exported': False}

            print("\n[Wayback Links]")
            for link in r_data:
                print(link)
        else:
            print_status(r_sc, Color.RED, 'Fetching URLs')
    
    except requests.exceptions.RequestException as e:
        print(f'\n{Color.RED}[-] Exception : {Color.CYAN}{e}{Color.RESET}')
    except Exception as e:
        print(f'\n{Color.RED}[-] Exception : {Color.CYAN}{e}{Color.RESET}')


if __name__ == '__main__':
    target = input(Color.YELLOW + "Enter the domain name (example.com): "+Color.RESET)
    fetch_wayback_links(target)