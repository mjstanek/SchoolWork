# Name: Matt Stanek
# Date: 4/2/2025

import shodan
import re
from dotenv import load_dotenv
import os

def verify_api_key(api_key):
    is_valid = False
    pattern = re.compile(r'^[a-zA-Z0-9]{32}$')
    is_match = pattern.findall(api_key)
    if is_match:
       is_valid = True
    else:
       is_valid = False

    return is_valid

def run_search(shodan_api):
   keyword = input("Please enter a keyword to search: ")
   if not keyword or len(keyword) < 3 or len(keyword) > 50:
    raise ValueError
   else:
      results = shodan_api.search(keyword,2)
      print(f"Results found: {results['total']}")
      for result in results['matches']:
        print(f"IP: {result['ip_str']}")
        print(f"Domain: {result['domains']}")
        print(f"Hostnames: {result['hostnames']}")
        print(f"Organization: {result['org']}")
        print(f"Location: {result['location']}")
        print("-" * 40)

def main():
    try:
        load_dotenv()
        api_key = os.getenv("SHODAN_API_KEY")
        if verify_api_key(api_key):
            shodan_api = shodan.Shodan(api_key)
            run_search(shodan_api)
    except ValueError:
        print("Invalid keyword. Please enter a keyword between 3 and 50 characters.")
    except KeyError:
        print("API key not found. Please set the SHODAN_API_KEY environment variable.")
    except:
        print("An unexpected error occurred. Please check your input and try again.")

main()