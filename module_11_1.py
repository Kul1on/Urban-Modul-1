import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
data = response.json()
print("Данные о курсах валют:", data)

df = pd.DataFrame(data['rates'].items(), columns=['Currency', 'Rate'])
print("\nТаблица курсов валют:\n", df)

average_rate = df['Rate'].mean()
max_rate = df['Rate'].max()
min_rate = df['Rate'].min()
print(f"\nСредний курс: {average_rate:.2f}, Максимальный курс: {max_rate:.2f}, Минимальный курс: {min_rate:.2f}")

plt.figure(figsize=(10, 5))
plt.bar(df['Currency'], df['Rate'], color='blue')
plt.xlabel('Валюта')
plt.ylabel('Курс')
plt.title('Курсы валют относительно USD')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('currency_rates.png')
plt.show()
