#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import re
import codecs
from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3
import sqlite3 as lite
from operator import itemgetter
from datetime import datetime, timedelta

# from HTMLParser import HTMLParser
# from IPython.core.debugger import Tracer

# get rid of a warning message
requests.packages.urllib3.disable_warnings()

reload(sys)
sys.setdefaultencoding('utf8')
currentDate = datetime.today().strftime('%Y-%m-%d')

def connectDB():

      db_file = dir_path + "/win_los.sqlite"
      return  lite.connect(db_file)


entries = []

def get_tables_data(tables):
    for tr in tables[0].find_all("tr"):
    	win = []
        # print tr.find_all("a", class_="link")[0].string.encode('utf-8')
        sname = tr.find_all("a", class_="link")[0].string.encode('utf-8')
        win.append(sname.strip())
        # print tr.find_all("a", class_="link")[0].get('href')
        slink =  tr.find_all("a", class_="link")[0].get('href').replace("/aktier/om-aktien.html/", "")
        win.append(slink)
        # print tr.find("td", class_="positive changePercent").string.encode('utf-8')
        pchange = tr.find("td", class_="positive changePercent").string.encode('utf-8').replace(",", ".")
        win.append(pchange)
        plast = tr.find("td", class_="lastPrice last").string.encode('utf-8').replace(",", ".")
        win.append(plast)
        win.append(currentDate)
        win.append("W")
        entries.append(win)

    for tr in tables[1].find_all("tr"):
    	los = []
        sname = tr.find_all("a", class_="link")[0].string.encode('utf-8')
        los.append(sname.strip())
        # print tr.find_all("a", class_="link")[0].get('href')
        slink = tr.find_all("a", class_="link")[0].get('href').replace("/aktier/om-aktien.html/", "")
        los.append(slink)
        # print tr.find("td", class_="negative changePercent").string.encode('utf-8')
        pchange = tr.find("td", class_="negative changePercent").string.encode('utf-8').replace(",", ".")
        los.append(pchange)
        plast = tr.find("td", class_="lastPrice last").string.encode('utf-8').replace(",", ".")
        los.append(plast)
        los.append(currentDate)
        los.append("L")
        entries.append(los)
    return entries


# url = "file:///Users/valentingeorgiev/dev/winners_loosers/2016-12-14-vinnare-forlorare.html"
# url = "https://www.avanza.se/marknadsoversikt.html"
# url_all = "https://www.avanza.se/aktier/vinnare-forlorare.html"
# r = requests.get(url_all)
# data = r.text
# soup = BeautifulSoup(data, "lxml")
# all_tables = soup.find_all("tbody")
# print "==All stocks=="
# get_tables_data(all_tables)

# print len(soup.find_all("table"))
# print len(all_tables)
# print len(all_tables[0].contents)

url_stchlm = "https://www.avanza.se/aktier/vinnare-forlorare.html?countryCode=SE&marketPlaceCodes=XSTO&timeUnit=TODAY"
r = requests.get(url_stchlm)
data = r.text
soup = BeautifulSoup(data, "lxml")
all_tables = soup.find_all("tbody")
# print "\n ==XSTO stocks=="
res = get_tables_data(all_tables)

dir_path = os.path.dirname(os.path.realpath(__file__))
db = connectDB()
db = connectDB()
cur = db.cursor()

for r in res:
	query = u"INSERT INTO win_los (sname, slink, pchange, plast, date, type) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" % (r[0], r[1], r[2], r[3], r[4], r[5])
	cur.execute(query)
	db.commit()
	# print r
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
