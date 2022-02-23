import re

# Open and read HTML file found - utilises the HTML without any newlines and tabs
file = open("tablePageStripped.html")
sourceContent = file.read()
file.close()

# Task 1: Get content of table which is within the tbody tag
def tbodyContentExtractor(source):
  pass

# Task 2: Get all rows in table
def rowExtractor(source):
  pass

# Task 3: Find out any titles (if any)
def findTitles(rows):
  pass

tableContent = tbodyContentExtractor(sourceContent)
rows = rowExtractor(tableContent)
titles = findTitles(rows)

print(titles)