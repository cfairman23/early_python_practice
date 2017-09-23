## List of dictionaries 
suppliers = [{"name" : "supplier 1", "price" : 90, "distance": 6, "Friendly" : 1},
			 {"name" : "supplier 2", "price" : 75, "distance" : 5, "Friendly" : 0},
			 {"name" : "supplier 3", "price" : 120, "distance" : 12, "Friendly" : 0},
			 {"name" : "supplier 4", "price" : 130, "distance" : 6, "Friendly" : 1},
			 {"name" : "supplier 5", "price" : 60, "distance" : 9, "Friendly" : 1}]

def is_close(supplier):
	return supplier["distance"] < 10

def is_cheap(supplier):
	return supplier["price"] < 100

def is_friendly(supplier):
	return supplier["Friendly"] > 0

## Function that finds cheap, close, and friendly suppliers 
## and creates/returns a new list only consisting of those suppliers
def get_cheap_close_friendly_suppliers(list_of_suppliers):
	cheap_close_friendly_suppliers = []
	for supplier in suppliers:
		if is_close(supplier) and is_cheap(supplier) and is_friendly:
			cheap_close_friendly_suppliers.append(supplier) 	
	return cheap_close_friendly_suppliers

## Prints out the list we created of cheap, close, and friendly suppliers
cheap_close_friendly_suppliers = get_cheap_close_friendly_suppliers(suppliers)
print(cheap_close_friendly_suppliers)
