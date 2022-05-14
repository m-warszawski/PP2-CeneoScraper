import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista opiniii
print("Zapisane opinie: ")
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
print("--------------------")

product_id = input("Podaj ID produktu:\n").strip()
opinions = pd.read_json(f"opinions/{product_id}.json")

# Dane liczbowe
opinions_count = len(opinions)
print(f"Liczba opinii: {opinions_count}")
advantages_count = opinions["advantages"].map(bool).sum()
print(f"Liczba opinii z listą zalet: {advantages_count}")
defects_count = opinions["defects"].map(bool).sum()
print(f"Liczba opinii z listą wad: {defects_count}")
average_score = opinions["stars"].mean().round(2)
print(f"Średnia ocena produktu: {average_score}")

# Folder
directory = "plots"
try:
    os.stat(directory)
except:
    os.mkdir(directory)

# Wykresy
recommendation = opinions["recommendation"].value_counts(dropna=False).sort_index().reindex(["Nie polecam", "Polecam", None], fill_value=0)
recommendation.plot.pie(
    label="",
    autopct= lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"]
)
plt.title("Rekomendacje")
plt.savefig(f"plots/{product_id}_recommendations.png")
plt.close()
print("Zapisano wyres rekomendacji!")

stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,0.5,0.5)), fill_value=0)
stars.plot.bar(
    color="red"
)
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.show()