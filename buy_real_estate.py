houses = [{"name" : "house 1", 
		  "original_price" : 500000, 
		  "current_price" : 750000 }, 
		  {"name" : "house 2", 
		  "original_price" : 125000,
		  "current_price" : 150000},
		  {"name" : "house 3",
		  "original_price" : 100000,
		  "current_price" : 110000},
		  {"name" : "house 4",
		  "original_price" : 600000,
		  "current_price" : 790000},
		  {"name" : "house 5",
		  "original_price" : 1000000,
		  "current_price" : 1500000}]

total_price_change = 0

for house in houses:
	price_change = house["current_price"] - house["original_price"]
	total_price_change += price_change

## The below needs to be un-indented so that the compiler doesn't think
## it is part of the for-loop
avg_price_change = total_price_change / len(houses)
print(str(avg_price_change))