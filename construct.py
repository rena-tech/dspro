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