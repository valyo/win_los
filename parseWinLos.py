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

      db_file = dir_path + "/win_los.db"
      return  lite.connect(db_file)

dir_path = os.path.dirname(os.path.realpath(__file__))
db = connectDB()
cur = db.cursor()
for stock in stocks:

	stock[2] = stock[2].replace("[u'", "")
	stock[2] = stock[2].replace("']", "")
	stock[1] = stock[1].replace("/aktier/om-aktien.html/", "")
	print stock
	query = u"INSERT INTO win_los (sname, slink, pchange, date) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');" % (stock[0], stock[1], stock[2], stock[3])
	cur.execute(query)

db.commit()



