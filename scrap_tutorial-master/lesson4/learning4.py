import requests
import re
import json
import time
import random
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm

folder_path = Path("scrap_tutorial-master/lesson4/")

# person_url_list = []

# for i in range(0, 634, 12):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/1055588-1055588?limit=12&noFilterSet=true&offset={i}"

#     q = requests.get(url)
#     result = q.content

#     soup = BeautifulSoup(result, 'lxml')

#     persons = soup.find_all(class_="bt-slide-content")

#     for person in persons:
#         person_page_url = person.find('a').get('href')
#         person_url_list.append(person_page_url)

# with open(folder_path / "person_url_list.txt", "a") as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")

with open(folder_path / "person_url_list.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []

    count = 0

    for line in tqdm(lines, desc="Scraping members"):
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person_name = soup.find(class_="m-biography__introName").text

        person_company = soup.find(
            class_="m-biography__introInfo").get_text(strip=True, separator=' ')

        try:
            target_h2 = soup.find(
                "h2", string=re.compile("Profile im Internet"))

            social_list = target_h2.find_next("ul", class_="e-linkList")

            social_networks = social_list.find_all("a")

            social_networks_urls = []
            for network in social_networks:
                social_networks_urls.append(network.get('href'))

        except Exception:
            social_networks_urls = []

        data = {
            "person_name": person_name,
            "person_company": person_company,
            "social_networks": social_networks_urls
        }

        count += 1

        print(f"#{count}: {line} is done!", flush=True)

        data_dict.append(data)

        time.sleep(random.randrange(2, 4))

        with open(folder_path / "data.json", "w", encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
