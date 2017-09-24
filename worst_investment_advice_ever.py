## This program creates a list of dictionaries of the companies whose revenue exceeds a certain number. The program then prints out
## a statement recommending you to buy the stock of the compananies in the list created.
## Do not use this to influence your stock buying behavior. I just wanted to practice importing data from Quandl. 
## There is not necessarily a correlation between a company's revenue and its stock price. If a company's revenue is high,
## It doesn't mean that you should buy its stock.

import quandl
import csv

quandl.ApiConfig.api_key = "q-EqxJQn4rH41BP7Ncom"
quandl.ApiConfig.api_version = '2015-04-09'

stocks = []
best = []
with open("ZACKS-CP.csv","r") as csvfile:
	csv_reader = csv.reader(csvfile)
	csv_as_list = list(csv_reader)
	column_title_row = True

	for row in csv_as_list:
		if column_title_row:
			column_title_row = False
		else:
			stock_dictionary = {}
			ticker_symbol = row[0]
			tot_revenue = row[29]
			stock_dictionary["stock_ticket"] = ticker_symbol
			stock_dictionary["tot_revenue"] = tot_revenue
			stocks.append(stock_dictionary)

	for each_stock in stocks:
		if  float(each_stock["tot_revenue"]) > 100000:
			best.append(each_stock)

best_names = [dic["stock_ticket"] for dic in best]

print("You should buy these stocks!!! " + str(best_names))








