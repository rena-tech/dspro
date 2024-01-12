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

# SQLiteデータベースへの接続とテーブルの作成
conn = sqlite3.connect('sleep_data.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS sleep_data (Country TEXT, SleepTime TEXT, Population TEXT)')
conn.commit()

# データの挿入
for row in data:
    cursor.execute('INSERT INTO sleep_data VALUES (?, ?, ?)', row)

conn.commit()
conn.close()

# ータベースからデータを取得
conn = sqlite3.connect('sleep_data.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM sleep_data')
result = cursor.fetchall()

# CSVファイルに保存
csv_file_path = 'sleep_data_from_db.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(result)

# データのクリーニング
cleaned_data = [[cell.strip() for cell in row] for row in result]

# データの可視化
sleep_times = [row[1] for row in cleaned_data if row[1]]
plt.bar([row[0] for row in cleaned_data], sleep_times)
plt.xlabel('Country')
plt.ylabel('Sleep Time')
plt.title('Sleep Time by Country (from Database)')
plt.xticks(rotation=90)
plt.show()

# コネクションのクローズ
conn.close()
