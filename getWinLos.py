#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import re
import codecs
from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
from operator import itemgetter
# from HTMLParser import HTMLParser
# from IPython.core.debugger import Tracer

# try:
#     output_file = sys.argv[1]
# except:
#     sys.exit("no output file specified!")
def get_tables_data(tables):
    for tr in tables[0].find_all("tr"):
        print tr.find_all("a", class_="link")[0].string.encode('utf-8')
        print tr.find_all("a", class_="link")[0].get('href')
        print tr.find("td", class_="positive changePercent").string.encode('utf-8')

    for tr in tables[1].find_all("tr"):
        print tr.find_all("a", class_="link")[0].string.encode('utf-8')
        print tr.find_all("a", class_="link")[0].get('href')
        print tr.find("td", class_="negative changePercent").string.encode('utf-8')


# url = "file:///Users/valentingeorgiev/dev/winners_loosers/2016-12-14-vinnare-forlorare.html"
# url = "https://www.avanza.se/marknadsoversikt.html"
url_all = "https://www.avanza.se/aktier/vinnare-forlorare.html"
r = requests.get(url_all)
data = r.text
soup = BeautifulSoup(data, "lxml")
all_tables = soup.find_all("tbody")
print "==All stocks=="
get_tables_data(all_tables)

# print len(soup.find_all("table"))
# print len(all_tables)
# print len(all_tables[0].contents)

url_stchlm = "https://www.avanza.se/aktier/vinnare-forlorare.html?countryCode=SE&marketPlaceCodes=XSTO&timeUnit=TODAY"
r = requests.get(url_stchlm)
data = r.text
soup = BeautifulSoup(data, "lxml")
all_tables = soup.find_all("tbody")
print "\n ==XSTO stocks=="
get_tables_data(all_tables)
# print all_tables[1].find_all("tr")[0].find_all("a", class_="link")[0].get('href')

# for tr in all_tables[0].find_all("tr"):
#     print tr.find_all("a", class_="link")[0].string.encode('utf-8')
#     print tr.find_all("a", class_="link")[0].get('href')
#     print tr.find("td", class_="positive changePercent").contents
#
# for tr in all_tables[1].find_all("tr"):
#     print tr.find_all("a", class_="link")[0].string.encode('utf-8')
#     print tr.find_all("a", class_="link")[0].get('href')
#     print tr.find("td", class_="negative changePercent").contents

# print len(all_tables[0].find_all("a", class_="link"))


# print len(all_tables[0].find_all("a", class_="link"))
# for link in all_tables[0].find_all("a", class_="link"):
#     print link
#     print "bang"


# for cont in all_tables[0].contents:
#     print cont
#     print "bang"

# print all_tables[6]['class']
# for child in all_tables[0].descendants:
#     print "bang"
#     print child


# print all_tables[0].prettify().encode('utf-8')


# with codecs.open(output_file, 'w', 'utf-8') as output:
#     output.write(all_tables[0].prettify())
# print soup.find_all['positive changePercent']
