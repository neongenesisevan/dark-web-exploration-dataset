"""
Initially used for applying hashtags to pseudonyms
"""

import pandas as pd

df = pd.read_excel("./findings_release.ods", engine="odf")

names = df["Name (pseudonyms)"]
name_dict = {}
unique_names = []

for name in names:
    if name in name_dict.keys():
        name_dict[name] += 1
    else:
        name_dict[name] = 1
    unique_names.append(f"{name} #{name_dict[name]}")

with open("names2.csv", "w") as file:
    text = "Name (pseudonyms)" + "\n"

    for name in unique_names:
        text += f"\"{name}\"" + "\n"

    file.write(text)