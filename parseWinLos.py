import re
import os
import sqlite3 as lite
import codecs

hand = codecs.open('2017-12-12-vinnare-forlorareNew.txt', encoding='utf-8')
numbers = list()

entries = []
stocks = []
xsto = False
for line in hand:
   if "==XSTO stocks==" in line:
      xsto = True
      continue

   if xsto:
      # print line
      if len(line.strip()) == 0:
         if len(entries) == 3:
            entries.append("2017-12-12")

         if len(entries) > 0:
            stocks.append(entries)

         entries = []
         continue

      entries.append(line.strip())

def connectDB():

      db_file = dir_path + "/win_los.sqlite"
      return  lite.connect(db_file)

dir_path = os.path.dirname(os.path.realpath(__file__))
db = connectDB()
cur = db.cursor()
for stock in stocks:

	sname = stock[0]
	pchange = stock[2].replace("[u'", "")
	pchange = pchange.replace("']", "")
	pchange = pchange.replace(",", ".")
	if "-" in pchange:
		typ = "L"
	else:
		typ = "W"
	slink = stock[1].replace("/aktier/om-aktien.html/", "")
	# print stock
	# print sname + "," + slink + "," + pchange + "," + stock[3] + "," + typ
	# query = u"INSERT INTO win_los (sname, slink, pchange, date) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');" % (stock[0], stock[1], stock[2], stock[3])
	query = u"INSERT INTO win_los (sname, slink, pchange, date, type) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');" % (sname, slink, pchange, stock[3], typ)
	cur.execute(query)

db.commit()



