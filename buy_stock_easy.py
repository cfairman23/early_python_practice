import csv

stocks = {}
with open("data/stocks.csv", "r") as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_as_list = list(csv_reader)
	collum_title_row = True
	for row in csv_as_list:
		if collum_title_row:
			collum_title_row = False
		else:
			ticker_symbol = row[0]
			company_name = row[1]
			opening_price = row[2]
			closing_price = row[3]

price_as_string = input("What is the price of AAPL? ")
price_as_int = int(price_as_string)
if price_as_int > 170:
	print("Sell")
elif price_as_int < 160:
	print("Buy")