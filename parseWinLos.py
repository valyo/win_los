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
         	# print "bla"
            stocks.append(entries)
            # stocks.append("2017-12-12")
         entries = []
         continue

      entries.append(line.strip())

# print stocks[1]
for stock in stocks:
	print stock[3]




