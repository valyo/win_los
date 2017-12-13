import re

hand = open('2017-12-12-vinnare-forlorareNew.txt')
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


for stock in stocks:

	stock[2] = stock[2].replace("[u'", "")
	stock[2] = stock[2].replace("']", "")
	stock[1] = stock[1].replace("/aktier/om-aktien.html/", "")
	print stock





