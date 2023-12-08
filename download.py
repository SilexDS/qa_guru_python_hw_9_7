import os
import requests
from selene import query
from selene.support.shared import browser
from script_os import FILES_DIR


def test_download_pdf():
    # browser.open("https://filesamples.com/formats/pdf")
    # download_url = browser.element("body > div.container.mx-auto.py-3.md\:py-8.px-3.md\:px-2 > main > "
    #                                "div.grid.grid-cols-4.md\:gap-8 > div.md\:col-span-3.col-span-4 > div > "
    #                                "div:nth-child(1) > a").get(query.attribute("href"))
    # content = requests.get(url=download_url).content
    content = requests.get(url='https://filesamples.com/samples/document/pdf/sample3.pdf').content
    with open(os.path.join(FILES_DIR, "test_pdf.pdf"), 'wb') as file:
        file.write(content)

def test_download_xlsx():
    # browser.open("https://filesamples.com/formats/xlsx")
    # download_url = browser.element("body > div.container.mx-auto.py-3.md\:py-8.px-3.md\:px-2 > main > "
    #                                "div.grid.grid-cols-4.md\:gap-8 > div.md\:col-span-3.col-span-4 > div > "
    #                                "div:nth-child(1) > a").get(query.attribute("href"))
    # content = requests.get(url=download_url).content
    content = requests.get(url='https://filesamples.com/samples/document/xlsx/sample3.xlsx').content
    with open(os.path.join(FILES_DIR, "test_xlsx.xlsx"), 'wb') as file:
        file.write(content)

def test_download_csv():
    # browser.open("https://filesamples.com/formats/csv")
    # download_url = browser.element("body > div.container.mx-auto.py-3.md\:py-8.px-3.md\:px-2 > main > "
    #                                "div.grid.grid-cols-4.md\:gap-8 > div.md\:col-span-3.col-span-4 > div > "
    #                                "div:nth-child(1) > a").get(query.attribute("href"))
    # content = requests.get(url=download_url).content
    content = requests.get(url='https://filesamples.com/samples/document/csv/sample3.csv').content
    with open(os.path.join(FILES_DIR, "test_csv.csv"), 'wb') as file:
        file.write(content)