from itertools import product
from string import ascii_lowercase
import numpy
import requests
import time
import concurrent.futures

base_url = "https://ggez.ch/"
key_urls = [base_url + ''.join(i) for i in product(ascii_lowercase, repeat=1)]
split_urls = numpy.array_split(key_urls, 52)
header = { 'User-Agent': '' }

def iter_req(target_urls):
    for url in target_urls:
        requests.head(url, headers=header)

confirm = input("FIRE?")
start = time.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    pool = executor.map(iter_req, split_urls)

print(f'Ran {len(key_urls)} urls in {(time.time() - start)} seconds')