import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import matplotlib.pyplot as plt

# データの取得
url = "https://zomasleep.com/blog/whos-getting-the-most-sleep"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 表の抽出
    table = soup.find('table')

    # 表の各行を取得
    rows = table.find_all('tr')

    # ヘッダーの取得
    header = [header.text.strip() for header in rows[0].find_all('th')]

    # データの取得
    data = []
    for row in rows[1:]:
        row_data = [cell.text.strip() for cell in row.find_all('td')]
        data.append(row_data)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)