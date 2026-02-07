import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Путь к файлу с данными
file_path = "c:\\Users\\ryago\\OneDrive\\Desktop\\Уник\\python\\events-1.json"

# Этап 1. Чтение JSON-файла и загрузка в DataFrame
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data["events"])

print("Тип df:", type(df))
print("Первые 5 строк:")
print(df.head())

# Этап 2. Анализ распределения по типам событий (signature)
print("\nЧастота типов событий (signature):")
signature_counts_series = df["signature"].value_counts()
print(signature_counts_series)

# Переводим в DataFrame для удобной визуализации
signature_counts = signature_counts_series.reset_index()
signature_counts.columns = ["signature", "count"]

# Этап 3. Визуализация распределения типов событий
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))

# Сортируем по убыванию, чтобы самый частый был сверху
sorted_counts = signature_counts.sort_values("count", ascending=False)

ax = sns.barplot(
    data=sorted_counts,
    y="signature",
    x="count",
    palette="Blues_r"
)

plt.title("Распределение типов событий безопасности")
plt.xlabel("Количество событий")
plt.ylabel("Тип события (signature)")

# Подписи значений на барах
for i, (count) in enumerate(sorted_counts["count"]):
    ax.text(
        x=count + 0.1,
        y=i,
        s=str(count),
        va="center"
    )

plt.tight_layout()
plt.show()
