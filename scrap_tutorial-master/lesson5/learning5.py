import requests
import lxml
import json
import re
import html
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm

folder_path = Path("scrap_tutorial-master/lesson5/")

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

fests_urls_list = []
for i in range(0, 451, 15):
    # for i in range(0, 15, 15):
    url = f"https://www.skiddle.com/news/festivals/{i}"

    req = requests.get(url=url, headers=headers)

    # with open(f"{folder_path}/data/index_{i}.html", "w", encoding="utf-8") as file:
    #     file.write(req.text)

    # with open(f"{folder_path}/data/index_{i}.html", encoding="utf-8") as file:
    #     src = file.read()

    soup = BeautifulSoup(req.text, 'lxml')

    cards = soup.find_all('a', class_="card-img-link")

    for item in cards:
        fest_url = "https://www.skiddle.com/" + item.get('href')
        fests_urls_list.append(fest_url)

count = 0
fest_list_result = []
for url in tqdm(fests_urls_list, desc="Scraping festivals"):
    count += 1
    print(count, flush=True)
    print(url, flush=True)

    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')

        fest_info_block = soup.find('span', id='breadcrumb-crumbs')

        fest_name = fest_info_block.contents[-1].strip().lstrip('»').strip()

        fest_date_place_block = soup.find('script', type='application/ld+json')

        fest_date = "Не найдена"
        fest_location_url = "Ссылка не найдена"

        if fest_date_place_block:
            data = json.loads(
                fest_date_place_block.string.strip(), strict=False)
            article_body = data.get('articleBody', '')

            clean_text = ""
            if article_body:
                clean_text = html.unescape(article_body)
                clean_text = re.sub(r'<[^>]+>', '', clean_text)

            date_match = re.search(
                r'(?:\w+day,?\s)?\d{1,2}(?:st|nd|rd|th)?\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}', clean_text)

            if date_match:
                fest_date = date_match.group(0)
            elif "later this month" in clean_text.lower():
                fest_date = "Later this month"
            elif "this summer" in clean_text.lower():
                fest_date = "This summer"
            else:
                raw_date = data.get('startDate') or data.get(
                    'datePublished', 'Не найдена')
                fest_date = raw_date.split(
                    'T')[0] if 'T' in raw_date else raw_date

            content_soup = BeautifulSoup(html.unescape(article_body), 'lxml')
            links = content_soup.find_all('a', href=True)

            for link in links:
                href = link['href']
                clean_href = href.split('?')[0].strip('/')
                path_parts = clean_href.split('/')

                if 'whats-on' in path_parts and len(path_parts) >= 3:
                    fest_location_url = href
                    if not fest_location_url.startswith('http'):
                        fest_location_url = "https://skiddle.com" + fest_location_url
                    break

                elif any(word in link.text for word in ['Park', 'Warehouse', 'Arena', 'Club', 'Stadium']):
                    fest_location_url = href
                    if not fest_location_url.startswith('http'):
                        fest_location_url = "https://skiddle.com" + fest_location_url
                    break

            contact_details_dict = {}
            if fest_location_url.startswith('http'):
                try:
                    req_venue = requests.get(
                        url=fest_location_url, headers=headers, timeout=10)
                    soup_venue = BeautifulSoup(req_venue.text, 'lxml')

                    target_keys = ['Venue Name', 'Venue Short Url',
                                   'Address', 'Postcode', 'Town', 'Type of venue']

                    for key in target_keys:
                        label = soup_venue.find(lambda tag: tag.name in [
                                                'p', 'div', 'span'] and tag.get_text().strip() == key)

                        if label:
                            # Поднимаемся к родителю-контейнеру (ячейке сетки)
                            container = label.find_parent(['div', 'span'])

                            # Собираем весь текст внутри ячейки
                            all_texts = [t.get_text().strip() for t in container.find_all(
                                ['p', 'div', 'span', 'a'])]

                            # Значение — это текст, который НЕ равен заголовку (key) и не пустой
                            value = next(
                                (t for t in all_texts if t != key and t != ""), "Инфо отсутствует")

                            contact_details_dict[key] = value
                        else:
                            contact_details_dict[key] = "Поле не найдено"

                except Exception as e:
                    print(
                        f"Ошибка сбора контактов на {fest_location_url}: {e}")
            else:
                print(f"Пропуск: Ссылка на локацию не найдена для {fest_name}")

            fest_list_result.append(
                {
                    "Fest name": fest_name,
                    "Fest date": fest_date,
                    "Contacts data": contact_details_dict
                }
            )

    except Exception as e:
        print(f"Error on {url}: {e}")

with open(f"{folder_path}/data/fest_list_result.json", "a", encoding="utf-8") as json_file:
    json.dump(fest_list_result, json_file, indent=4, ensure_ascii=False)
