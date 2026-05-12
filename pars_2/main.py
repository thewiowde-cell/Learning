import requests
import fake_useragent
import time
import random
import re
import json
import multiprocessing
import aiohttp
import asyncio
from bs4 import BeautifulSoup

# user = fake_useragent.UserAgent().random

# header = {
#     "User-Agent": user
# }

# # url = "https://icanhazip.com/"
# # req = requests.get(url)
# # print(req.status_code)
# # print(req.text)

# url = "https://browser-info.ru/"
# req = requests.get(url, headers=header)
# src = req.text

# soup = BeautifulSoup(src, 'lxml')

# block = soup.find('div', id="tool_padding")
# check_js = block.find('div', id="javascript_check")
# status_js = check_js.find_all('span')[1]
# result_js = f"javascript: {status_js.text}"

# check_flash = block.find('div', id="flash_version")
# status_flash = check_flash.find_all('span')[1]
# result_flash = f"flash: {status_flash.text}"

# check_user = block.find('div', id="user_agent").text

# print(status_js.text)
# print(status_flash.text)
# print(check_user)

# session = requests.Session()

# user = fake_useragent.UserAgent().random

# header = {
#     "User-Agent": user
# }

# url = "https://www.rusforum.com/login.php?do=login"

# data = {
#     "from_sent": "1",
#     "vb_login_username": "ddsads",
#     "vb_login_password": "",
# }

# req = session.post(url, headers=header, data=data)


# profile_info = "https://www.rusforum.com/profile.php"
# profile_req = session.get(profile_info).text


# cookies = [
#     {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
#     for key in session.cookies
# ]

# session2 = requests.Session()

# for cookie in cookies:
#     session2.cookies.set(**cookie)

# resp = session2.get(profile_info, headers=header)
# print(resp.text)

# # Lesson № 4
# session = requests.Session()

# image_number = 1
# storage_number = 1
# url = "https://zastavok.net"

# for storage in range(3150):
#     user = fake_useragent.UserAgent().random

#     header = {
#         "User-Agent": user
#     }

#     try:
#         req = requests.get(f"{url}/{storage_number}",
#                            headers=header, timeout=5)
#         src = req.text
#         soup = BeautifulSoup(src, 'lxml')

#         block = soup.find('div', class_='block-photo')

#         if not block:
#             print(
#                 f"Похоже, на странице {storage_number} нет фото или нас забанили.")
#             break

#         images = block.find_all('div', class_="short_full")

#         for image in images:
#             image_link = image.find('a').get('href')
#             download_storage = session.get(
#                 f"{url}{image_link}", headers=header, timeout=5)
#             src = download_storage.text

#             download_soup = BeautifulSoup(src, 'lxml')
#             download_block = download_soup.find(
#                 'div', class_="image_data").find('div', class_="block_down")

#             result_link = url + download_block.find('a').get('href')

#             image_bytes = session.get(result_link, headers=header, timeout=5)
#             src = image_bytes.content

#             with open(f"pars_2/image/{image_number}.jpg", 'wb') as file:
#                 file.write(src)

#             print(
#                 f"Загружено изображение {image_number} из {storage_number} страницы", flush=True)

#             image_number += 1

#             time.sleep(random.uniform(3, 6))

#     except Exception as e:
#         print(f"Ошибка на странице {storage_number}: {e}")
#         time.sleep(10)

#     storage_number += 1

# for proxy in proxy_base:
#     proxies = {
#         "http": f"http://{proxy}",
#         "https": f"http://{proxy}",
#     }

#     url = "https://icanhazip.com/"
#     try:
#         req = requests.get(url, proxies=proxies, timeout=2)
#         src = req.text
#         print(f"IP: {src}")
#     except Exception as e:
#         print(f"Прокси {proxy} не работает: {e}")

# # Lesson 5
# url = "https://proxyscrape.com"


# def handler(proxy):
#     proxies = {
#         "http": f"http://{proxy}",
#         "https": f"http://{proxy}",
#     }

#     try:
#         req = requests.get(url, proxies=proxies, timeout=5)
#         print(f"Прокси {proxy} РАБОТАЕТ! IP: {req.text.strip()}")
#     except Exception:
#         print(f"Прокси {proxy} не отвечает.")


# def download_real_proxies():
#     try:
#         req = requests.get(url)
#         if req.status_code == 200:
#             with open('pars_2/proxy', 'w', encoding='utf-8') as file:
#                 file.write(req.text.strip())
#             print("Файл 'proxy' обновлен реальными адресами!")
#     except Exception as e:
#         print(f"Ошибка при скачивании: {e}")


# download_real_proxies()

# with open('pars_2/proxy', encoding='utf-8') as file:
#     proxy_base = [line.strip() for line in file if line.strip()]

# with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
#     process.map(handler, proxy_base)


# def get_js(sp):
#     block = sp.find('div', id="javascript_check")
#     print(block.find_all('span')[1].text)


# def get_cookie(sp):
#     block = sp.find('div', id="cookie_check")
#     print(block.find_all('span')[1].text)


# def get_flash(sp):
#     block = sp.find('div', id="flash_version")
#     print(block.find_all('span')[1].text)


# def main():
#     url = "https://browser-info.ru/"

#     with open('pars_2/config.json') as json_file:
#         config = json.load(json_file)

#     req = requests.get(url)
#     src = req.text
#     soup = BeautifulSoup(src, 'lxml')

#     if config['js'] == True:
#         get_js(soup)
#     if config['cookie'] == True:
#         get_cookie(soup)
#     if config['flash'] == True:
#         get_flash(soup)


# if __name__ == '__main__':
#     main()

def get_proxies():
    url = "https://free-proxy-list.net/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    try:
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        proxies = []

        table = soup.find('table', class_='table-striped')
        rows = table.find('tbody').find_all('tr')

        proxies = []
        for row in rows:
            tds = row.find_all('td')
            if len(tds) > 1:
                ip = tds[0].text.strip()
                port = tds[1].text.strip()
                proxies.append(f"{ip}:{port}")

        return proxies
    except Exception as e:
        print(f"Ошибка при получении прокси: {e}")
        return []


proxy_list = get_proxies()

with open("pars_2/proxy", 'w', encoding='utf-8') as proxy_file:
    for proxy in proxy_list:
        proxy_file.write(f"{proxy}\n")

Categories = [
    "https://habr.com/ru/hubs/programming/articles/",
    "https://habr.com/ru/hubs/python/articles/",
]
