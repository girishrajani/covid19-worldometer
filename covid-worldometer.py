import requests
from bs4 import BeautifulSoup
URL = "https://www.worldometers.info/coronavirus/"
headers = {
    "User-Agents": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4080.0 Safari/537.36 Edg/82.0.453.2'}
page = requests.get(URL, headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.string

counter = soup.findAll(class_="maincounter-number")
counter1 = soup.findAll(class_="number-table-main")
counter2 = soup.findAll(class_="number-table")

total = counter[0].get_text().strip()
deaths = counter[1].get_text().strip()
recovered = counter[2].get_text().strip()

current = counter1[0].get_text().strip()
closed = counter1[1].get_text().strip()

deaths = counter2[3].get_text().strip()

print("COVID 19 WORLD Updates")
print("TOTAL NUMBER OF CASES "+total)
print("TOTAL NUMBER OF ACTIVE CASES "+current)
print("TOTAL NUMBER OF DEATHS "+deaths)
print("TOTAL NUMBER OF RECOVERD PATIENTS "+recovered)

