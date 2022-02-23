import re

# Open and read HTML file found - utilises the HTML without any newlines and tabs
file = open("tablePageStripped.html")
sourceContent = file.read()
file.close()

# RegEx patterns
tbodyPattern = "<tbody>(.*?)</tbody>"
trPattern = "<tr>(.*?)</tr>"
tdPattern = "<td>(.*?)</td>"
aPattern = "<a class=\"myTitle\".*?>(.*?)</a>"

# Task 1: Get content of table which is within the tbody tag
def tbodyContentExtractor(source):
  return re.findall(tbodyPattern, source)[0]

# Task 2: Get all rows in table
def rowExtractor(source):
  return re.findall(trPattern, source)

# Task 3: Find out any titles (if any)
def findTitles(rows):
  titles = []
  for item in rows:
    dataItems = re.findall(tdPattern, item)
    for dataItem in dataItems:
      aCheck = re.findall(aPattern, dataItem)
      if (len(aCheck) != 0):
        titles.append(aCheck[0])
  return titles

tableContent = tbodyContentExtractor(sourceContent)
rows = rowExtractor(tableContent)
titles = findTitles(rows)

print(titles)