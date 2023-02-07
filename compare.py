#!/usr/bin/env python

import webbrowser
import sys

"""
How to use me:
Pass arguments to the script:  ./compare.py 220 220r
or not, and we prompt for model numbers only, we glue the url together and open the browser.
"""

def create_end_url(a: list) -> str:
    return ',pa-'.join(a)

def main():
    a = sys.argv[1:]  ## a = args
    if a:
        models = create_end_url(a)
    else:
        a = []
        print("[q or enter to exit]")
        while True:
            model = input("Enter model number: ")
            if model == "q".lower() or model == "":
                break
            a.append(model)
        models = create_end_url(a)

    url = fr"https://www.paloaltonetworks.com/products/product-comparison?chosen=pa-{models}"

    print(url)
    webbrowser.open(url)

if __name__ == "__main__":
    main()
