## 3 dictionaries in one list
candidates = [{"name" : "Hilary", 
			   "money_raised" : 1000000,
			   "votes" : 25 },
 			  {"name" : "Donald", 
 			   "money_raised" : 5000000, 
 			   "votes" : 50}, 
				{"name" : "Bernie", 
				"money_raised" : 100, 
				"votes" : 10}]

candidates.append({"name" : "OMalley", "money_raised" : 600, "votes" : 5})

total_number_raised = candidates[0]["money_raised"] + candidates[1]["money_raised"] + candidates[2]["money_raised"] + candidates[3]["money_raised"]
print("In total, the candidates all raised " + str(total_number_raised) + " " "dollars")

total_votes = candidates[0] ["votes"] + candidates [1] ["votes"] + candidates [2] ["votes"] + candidates [3] ["votes"]
print("In total, there were " + str(total_votes) + " " + "votes")



