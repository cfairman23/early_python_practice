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




# data_goldmann = quandl.get_table('EOD/GS')
# data_jp_Morgan= quandl.get_table('EOD/JPM')
# data_intel = quandl.get_table('EOD/INTC')
# data_walmart = quandl.get_table('EOD/WMT')
# data_coca_cola = quandl.get_table('EOD/KO')



