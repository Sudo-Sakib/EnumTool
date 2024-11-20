import dns.resolver
import sys
from color import Color

def dnsrec(domain):
    try:
        result = {'dns': {}, 'dmarc': []}

        # Set a timeout value in seconds
        timeout = 10

        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']
        resolver.timeout = timeout
        resolver.lifetime = timeout

        # Supported DNS record types to query
        types = ['A', 'AAAA', 'CAA', 'CNAME', 'MX', 'NS', 'TXT']

        for record_type in types:
            try:
                response = resolver.resolve(domain, record_type)
                result['dns'][record_type] = [str(answer) for answer in response]
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
                pass

        dmarc_target = f'_dmarc.{domain}'
        try:
            dmarc_response = resolver.resolve(dmarc_target, 'TXT')
            result['dmarc'] = [str(answer) for answer in dmarc_response]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
            pass

        if result['dns'] or result['dmarc']:
            result['exported'] = True
        else:
            print(f'{Color.RED}[-] No DNS Records or DMARC Record Found!{Color.RESET}')
            result['exported'] = False

        return result

    except dns.resolver.NoNameservers as e:
        print(f'{Color.RED}[-] DNS Resolver Configuration Error: {e}{Color.RESET}')
        return None

def print_dns_result(result):
    if result:
        if result['exported']:
            print(f'[+] DNS Records:')
            for record_type, records in result['dns'].items():
                print(f'[+] {record_type}: {" | ".join(records)}')

            if result['dmarc']:
                print(f'[+] DMARC Records:')
                for dmarc_record in result['dmarc']:
                    print(f'    {dmarc_record}')
        else:
            print(f'{Color.RED}[-] No DNS Records or DMARC Record Found!{Color.RESET}')

if __name__ == "__main__":
    try:
        target_domain = input(f'{Color.YELLOW}Enter the domain to perform DNS enumeration: {Color.RESET}')
        result = dnsrec(target_domain)

        if result is not None:
            print_dns_result(result)
    except KeyboardInterrupt:
        print(f'{Color.RED}\nKeyboard interruption detected. Exiting...{Color.RESET}')
        
