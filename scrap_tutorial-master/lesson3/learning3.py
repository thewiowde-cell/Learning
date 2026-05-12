import requests
import json
import time
import random
import re
from bs4 import BeautifulSoup
from pathlib import Path


def get_url(url):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    }

    project_data_list = []

    iteration_count = 9
    print(f"Всего итераций: #{iteration_count}")

    for item in range(1, 10):
        req = requests.get(url + f"PAGEN_1={item}&PAGEN_2={item}", headers)

        folder_name = Path(f"scrap_tutorial-master/lesson3/data/data_{item}")

        if folder_name.exists():
            print("Папка уже существует!")
        else:
            folder_name.mkdir(parents=True)

        with open(f"{folder_name}/project_{item}.html", 'w', encoding='utf-8') as file:
            file.write(req.text)

        with open(f"{folder_name}/project_{item}.html", encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        articles = soup.find_all('article', class_='ib19')

        projects_urls = []
        for article in articles:
            project_url = "https://web.archive.org" + article.find(
                'div', class_='txtBlock').find('a').get('href')
            projects_urls.append(project_url)

        for project_url in projects_urls:
            req = requests.get(project_url, headers=headers)
            project_name = project_url.split('/')[-2]

            with open(f"{folder_name}/{project_name}.html", 'w', encoding='utf-8') as file:
                file.write(req.text)

            with open(f"{folder_name}/{project_name}.html", encoding='utf-8') as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')

            project_data = soup.find('div', class_='inside')

            try:
                projects_logo = "https://web.archive.org" + project_data.find(
                    'div', class_="Img logo").find('img').get('src')
            except Exception:
                projects_logo = "No project logo"

            try:
                project_name = project_data.find(
                    'div', class_='txt').find('h1').text
            except Exception:
                project_name = "No project name"

            try:
                project_short_discription = project_data.find(
                    'div', class_='txt').find('h4', class_='head').text
            except Exception:
                project_short_discription = "No project shortdiscription"

            try:
                project_website = project_data.find(
                    'div', class_='txt').find('p').find('a').text
            except Exception:
                project_website = "No project website"

            try:
                project_full_discription = project_data.find(
                    'div', class_='rBlock').find('p').text
            except Exception:
                project_full_discription = "No project full description"

            project_data_list.append(
                {
                    "Имя проекта": project_name,
                    "URL логотипа проекта": projects_logo,
                    "Краткое описание проекта": project_short_discription,
                    "Сайт проекта": project_website,
                    "Полное описание проекта": project_full_discription
                }
            )

            iteration_count -= 1
            print(
                f"Итерация {item} завершена, осталось итераций: #{iteration_count}")
            if iteration_count == 0:
                print("Все итерации завершены!")

            time.sleep(random.randrange(2, 4))

    with open("scrap_tutorial-master/lesson3/data/project_data.json", 'a', encoding='utf-8') as file:
        json.dump(project_data_list, file, indent=4, ensure_ascii=False)


def main():
    get_url("https://web.archive.org/web/20150901200643/http://www.edutainme.ru/edindex/ajax.php?params=%7B%22LETTER%22%3Anull%2C%22RESTART%22%3A%22N%22%2C%22CHECK_DATES%22%3Afalse%2C%22arrWHERE%22%3A%5B%22iblock_startaps%22%5D%2C%22arrFILTER%22%3A%5B%22iblock_startaps%22%5D%2C%22startups%22%3A%22Y%22%2C%22SHOW_WHERE%22%3Atrue%2C%22PAGE_RESULT_COUNT%22%3A9%2C%22CACHE_TYPE%22%3A%22A%22%2C%22CACHE_TIME%22%3A0%2C%22TAGS_SORT%22%3A%22NAME%22%2C%22TAGS_PAGE_ELEMENTS%22%3A%22999999999999999999%22%2C%22TAGS_PERIOD%22%3A%22%22%2C%22TAGS_URL_SEARCH%22%3A%22%22%2C%22TAGS_INHERIT%22%3A%22Y%22%2C%22SHOW_RATING%22%3A%22Y%22%2C%22FONT_MAX%22%3A%2214%22%2C%22FONT_MIN%22%3A%2214%22%2C%22COLOR_NEW%22%3A%22000000%22%2C%22COLOR_OLD%22%3A%22C8C8C8%22%2C%22PERIOD_NEW_TAGS%22%3A%22%22%2C%22DISPLAY_TOP_PAGER%22%3A%22N%22%2C%22DISPLAY_BOTTOM_PAGER%22%3A%22N%22%2C%22SHOW_CHAIN%22%3A%22Y%22%2C%22COLOR_TYPE%22%3A%22Y%22%2C%22WIDTH%22%3A%22100%25%22%2C%22USE_LANGUAGE_GUESS%22%3A%22N%22%2C%22PATH_TO_USER_PROFILE%22%3A%22%23SITE_DIR%23people%5C%2Fuser%5C%2F%23USER_ID%23%5C%2F%22%2C%22SHOW_WHEN%22%3Afalse%2C%22PAGER_TITLE%22%3A%22%5Cu0420%5Cu0435%5Cu0437%5Cu0443%5Cu043b%5Cu044c%5Cu0442%5Cu0430%5Cu0442%5Cu044b+%5Cu043f%5Cu043e%5Cu0438%5Cu0441%5Cu043a%5Cu0430%22%2C%22PAGER_SHOW_ALWAYS%22%3Atrue%2C%22USE_TITLE_RANK%22%3Afalse%2C%22PAGER_TEMPLATE%22%3A%22%22%2C%22DEFAULT_SORT%22%3A%22rank%22%2C%22noTitle%22%3A%22Y%22%7D&")


if __name__ == "__main__":
    main()
