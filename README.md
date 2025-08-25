Lazada Shop Scraper (Thailand)

Fetch product listings from selected Lazada Thailand stores and save them to plain-text files—one file per store.
Each output line is formatted as:

<product_name>|<image_url>|<sold_count>


⚠️ For educational and personal use. Respect Lazada’s Terms of Service and applicable laws.

Features

Scrapes multiple stores in one run (store_list).

Uses Lazada’s CSRF token endpoint to build valid requests.

Writes clean txt outputs per store.

Simple, dependency-light (only requests).

Requirements

Python 3.8+

Dependencies: requests

pip install requests

Quick Start

Save the script (e.g., scrape_lazada.py).

(Optional) Update the stores you want to scrape:

store_list = ['sandisk', 'kenvue', 'welcare-thailand']


Run it:

python scrape_lazada.py


Outputs will be created in the working directory:

sandisk.txt
kenvue.txt
welcare-thailand.txt


Example line:

SanDisk Ultra 128GB|https://.../image.jpg|1.2k sold


If the sold count is missing, the script writes 0.
