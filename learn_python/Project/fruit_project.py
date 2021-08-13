
Fruits = {} #Empty dictionary

while True:
	print("1. Add fruits")
	print("2. Delete fruits")
	print("3. Search fruit by name & rate")
	print("4. change fruit name and rate")
	print("5. Add to cart") 
	print("6. Display")
	print("7. Display the cart")
	print("8. Exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add Fruits
		fruit_id = input("\tEnter serial No ")
		if fruit_id not in Fruits.keys():
			f_name = input("\tEnter name ")
			rate = int(input("\tEnter rate "))
			impot_from = input("\tEnter the impot_from ")
			impot_date = input("\tEnter the impot_date ")
			buy_price = int(input("\tEnter the price"))
			temp ={
				"f_name":f_name,
				"rate":rate,
				"impot_from":impot_from,
				"impot_date":impot_date,
				"buy_price":buy_price
				}
			Fruits[fruit_id] = temp
		else:
			print("\t fruit id already Taken")
	
	elif ch == 2:
		#Delete Fruits
		fruit_id = input("\tEnter fruit id")
		if fruit_id  not in Fruits.keys():
			print("\tWrong fruit id")
		else:
			del Fruits[fruit_id]
	elif ch == 3:
		#Search fruit
		f_name = input("\tEnter name")
		found = False
		for i in Fruits.values():
			if i["f_name"] == f_name: # find name
				print(f"\t{i['f_name']} | {i['rate']} | {i['impot_from']} | {i['impot_date']} | {i['buy_price']}   ")
				found = True
				break
		
		if found == False :
			print("\tNot found")

	elif ch == 6:
		#Display fruits
		for fruit_id,fruit in Fruits.items():
			print(f"\t{fruit_id} | {fruit['f_name']} | {fruit['rate']} | {fruit['impot_from']} | {fruit['impot_date']} | {fruit['buy_price']}")
	elif ch== 4:
		#Change a fruit name & rate in the list
		fruit_id = input("\tEnter fruit id. ")
		if fruit_id not in Fruits.keys():
			print("\tWrong fruit id ")
		else:
			Fruits[fruit_id]['f_name'] = input("\tEnter new fruit name")


		fruit_id = input("\tEnter fruit id")
		if fruit_id not in Fruits.keys():
                        print("\tWrong fruit id")
		else: 
                        Fruits[fruit_id]['rate'] = input("\tEnter new rate")




	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")

