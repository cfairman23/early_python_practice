## Shows an implementation of the "two year rule"

import csv

stocks = []
with open("data/stocks.csv", "r") as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_as_list = list(csv_reader)
	collum_title_row = True
	for row in csv_as_list:
		if collum_title_row:
			collum_title_row = False
		else:
			stock = {} ## Making new dictionary for each stock

			stock["ticker_symbol"] = row[0] 
			stock["opening_price"] = row[3]
			stock["last_year_high"] = row[4]
			stock["last_year_low"] = row[5]

			## add these dictionaries to stocks dictionary

			stocks.append(stock)

			def recommended_sell(stocks2):
				recommended_sell = [] ## Making new list for recommended sell
				for stock in stocks2: ## taking in list of dictionaries "stock"
					if stock["opening_price"] > stock["last_year_high"]: ## checks key
						recommended_sell.append(stock) ## if fits stipulation, add to new list
				return recommended_sell ## needs return value
				## we have made a list of dictionaries fulfilling stipulations

			def recommended_buy(stocks3):
				recommended_buy = [] ## Making new list for recommended buy
				for stock in stocks3: ## Taking in list of dictionaries "stock"
					if stock["opening_price"] < stock["last_year_low"]: ## checks key
						recommended_buy.append(stock) ## add to new list
				return recommended_buy
				## we have made a list of dictionaries fulfilling stipulations

print("These are the recommended buy stocks: ", recommended_buy(stocks))
print("These are the recommended sell stocks: ", recommended_sell(stocks))





				


