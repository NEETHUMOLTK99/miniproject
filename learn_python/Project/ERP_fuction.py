#start a mini project console ERP system.
employees={}
teams = {} # create empty dictionry
def add_employee():
	employee_id = input("\tenter Employee id ")
	if employee_id not in employees.keys():
		name = input("\tenter name ")
		age = int(input("\tenter age "))
		gender = input("\tenter the gender ")
		place = input("\tenter place ")
		salary = int(input("\tenter salary "))
		previous_company = input("\tenter your previous company ")
		joining_date = input("\tenter joining date ")
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"previous_company":previous_company,
			"joining_date":joining_date,
			}
		employees[employee_id] = temp
	else:
			print("\tEmployee id  already Taken")

def delete_employee():
	eid = int(input("\tEnter employee id"))
	if eid not in employees.keys():
		print("\tWrong Employee id")
	else:
		del employees[employee_id]

def search_employee():
	name = input("\tEnter name")
	found = False
	for i in employees.values():
		if i["name"] == name: 
			print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
			found = True
			break
		if found==False:
			print("\tnot in the list")

def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")

def change_employee():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")
	cho =int(input("\tEnter your choice."))
	employee_id = input("\tEnter employee id.")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name") 
	elif cho == 2:
		employees[employee_id]['age'] = int(input("\tEnter new age"))
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender")
	elif cho == 4:
		employees[employee_id]['salary'] = int(input("\tEnter new salary"))
	else:
		print("invalid")




while True:
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("press 6 for Manage all Teams")
	print("Press 7 for Quit")
	ch = int(input("Enter choice"))
	if ch == 1:
	#adding employee
		add_employee()
			
	elif ch == 2:
	#delete
		delete_employee()
	elif ch == 3:
	#search
		search_employee()
	elif ch == 4:
	#display employee
		display_employee()
	elif ch== 5:
	#change employee details
		change_employee()
	elif ch == 6:
	#manage all Team
	elif ch == 7:

		break;
	else:
		print("Invalid Choice")




def manage_all_team_menu():
	print("\t1.Create Teams")
	print("\t2.Display Teams")
	print("\t3.Manage Teams(Particular)")
	print("\t4.Delete Teams")
	print("\t5.Exit")

def manage_all_teams():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create team
			create_team()
		elif ch == 2:
			#display teams
			display_teams()
		elif ch == 3:
			#Manage team(Particular)
			manage_team()
		elif ch == 4:
			#Delete Team
			delete_team()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")

def create_team():
	team_name = input("\tEnter team name ")
	teams[team_name] = []

def delete_team():
	team_name = input("\tEnter team name ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")

def display_teams():
	for key,value in teams.items(): #key is team_name,value is list of student serial no
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employees[i]["name"]
		print(f"{key} => {name_string}")
