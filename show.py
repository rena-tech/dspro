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