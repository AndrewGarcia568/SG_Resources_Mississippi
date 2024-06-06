# -*- coding: utf-8 -*-
"""
Created on Wed June 06 11:05:05 2024

@author: Micah Angelo Bacani
"""

from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import csv

base_url = "http://www.gasnom.com/ip/southernpines/oauc.cfm?dt="
header_data = []
main_data = []
rows = []

# construct url with "#month+#day%2C+#year&type=1"
month = "May"
day = "30"
year = "2024"
url = base_url + month + "+" + day + "%2C+" + year + "&type=1"

# creating html session to parse and load scripts
session = HTMLSession()
page = session.get(url)
page.html.render()

# create soup object for the whole rendered page
soup = bs(page.html.html, 'html.parser')

# get all table objects in the page
tables = soup.findAll('tbody')

# get header data
header_table = tables[0].findAll("tr")
for i in header_table:
    holder = i.findAll("td")
    for j in holder:
        if j.get_text(strip = True) != "":
            header_data.append(j.get_text(strip = True))

# get main table data
data_table = tables[2].findAll("tr")
for i in data_table:
    holder = i.findAll("td")
    rows = []
    for j in holder:
        rows.append(j.get_text(strip = True))
    if rows != ['']:
        main_data.append(rows)

#writing to csv
with open('SGResourcesMississippi-OperationallyAvailableCapacity-' + month + '-' + day + '-' + year + ".csv", 'w', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header_data)
    for i in main_data:
        writer.writerow(i)