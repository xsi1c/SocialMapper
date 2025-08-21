#!/usr/bin/env python3
import argparse
from src.social_mapper import SocialMapper
from colorama import Fore, Style, init

init(autoreset=True)

def print_results(results):
    for result in results:
        platform = result.get('platform', 'Unknown')
        if result.get('found') is True:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.GREEN}{platform}: FOUND{Style.RESET_ALL}")
            print(f"   |-- Profile Name: {result.get('profile_name', 'N/A')}")
            print(f"   |-- Profile URL: {result.get('url', 'N/A')}")
        elif result.get('found') is False:
            print(f"[{Fore.RED}-{Style.RESET_ALL}] {Fore.RED}{platform}: NOT FOUND{Style.RESET_ALL}")
        else:
            print(f"[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.YELLOW}{platform}: ERROR - {result.get('error', 'Unknown error')}{Style.RESET_ALL}")
        print()

def main():
    parser = argparse.ArgumentParser(description='SocialMapper - Find social media accounts by phone number.')
    parser.add_argument('phone_number', type=str, help='The phone number to search for (e.g., "+12345678900" or "2345678900")')
    args = parser.parse_args()

    try:
        print(f"[*] Initializing SocialMapper for: {args.phone_number}")
        mapper = SocialMapper(args.phone_number)
        print(f"[*] Running checks on {len(mapper.platform_checks)} platforms...\n")
        results = mapper.run_checks()
        print_results(results)

    except Exception as e:
        print(f"{Fore.RED}[!] Fatal Error: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
