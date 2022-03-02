import requests
from bs4 import BeautifulSoup
import pandas as pd

# Task 1: GET the source from the following URL: "https://table-page.herokuapp.com/"
plainText = requests.get("https://table-page.herokuapp.com/", headers={"user-agent": "Mozilla/6.0"})

# Task 2: Data extraction with BeautifulSoup
# Note: You have to use the text version of the Request object that is returned from above - i.e. pass in "plainText.text" instead of just "plainText"
page = BeautifulSoup(plainText.text, "html.parser")

# 1. Following the algorithm
titles = []
table = page.find("table")
tbody = table.find("tbody")
trs = tbody.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    for td in tds:
        value = td.find("a", {"class": "myTitle"})
        if value is not None:
            # BeautifulSoup.find() returns None if none found
            titles.append(value.text)

print(titles)

# 2. The more direct method
titles = []
allMatching = page.find_all("a", {"class": "myTitle"})
for title in allMatching:
  titles.append(title.text)

print(titles)

# Task 3 (Bonus): Playing around with Pandas.
df = pd.DataFrame(titles, columns=["URLs"])

print(df)

for index, row in df.iterrows():
    df.at[index, "URLs"] = row["URLs"] + ": the best website ever!"

print(df)