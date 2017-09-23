weight_str = input("The patient's weight is: ")
weight_int = int(weight_str)
if weight_int <= 50:
	print("The patient should receive 1 pill")
elif weight_int <= 100:
	print("The patient should receive 2 pills")
elif weight_int >= 150:
	print("The patient should receive 3 pills")
	

