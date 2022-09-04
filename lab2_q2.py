# empty dictionary is created
di = {}

while 1:
	# displaying options
	print("\n------ OPTIONS ----------")
	print("1. >> Create Empty Set")
	print("2. >> Insert")
	print("3. >> Delete")
	print("4. >> Search")
	print("5. >> Print")
	print("6. >> Union")
	print("7. >> Intersection")
	print("8. >> Set Difference")
	print("9. >> Symmetric Difference")
	print("10. >> Exit the program")
	print("---------------------------")
	choice = int(input("Select from the following options : "))

	# creating empty set
	if choice == 1:
		s = set({})
		# set name is used as key in dict
		setName = input("Enter the set name : ")
		di[setName] = s
		pass
	# inserting element into set
	elif choice == 2:
		setName = input("Enter set name : ")
		if setName in di.keys():
			di[setName].add(int(input("Enter a element : ")))
			print("Element inserted successfully..")
		else:
			print("Set name dNE")
		pass
	# deleting element in the set
	elif choice == 3:
		setName = input("Enter set Name : ")
		if setName in di.keys():
			elem = int(input("Enter the element that needs to be deleted : "))
			if elem in di[setName]:
				di[setName].remove(elem)
				print("Element deleted successfully...")
			else:
				print("Element dNE.. ")
		else:
			print("Set name dNE..")
		pass
	# searching element in a dictionary of particular set
	elif choice == 4:
		setName = input("Enter set name : ")
		if setName in di.keys():
			elem = int(input("Enter the element that to be searched : "))
			if elem in di[setName]:
				print("Element found..")
			else:
				print("Element dNE..")
		else:
			print("Set name dNE..")
		pass
	# printing set
	elif choice == 5:
		setName = input("Enter set name : ")
		if setName in di.keys():
			print(di[setName])
		else:
			print("Set name dNE..")
		pass
	# finding union of 2 sets
	elif choice == 6:
		setName1 = input("Enter 1st set name : ")
		if setName1 in di.keys():
			setName2 = input("Enter 2nd set name : ")
			if setName2 in di.keys():
				ans = di[setName1].union(di[setName2])
				print(ans)
			else:
				print("Set name dNE..")
		else:
			print("Set name dNE..")
		pass
	# finding intersection of two sets
	elif choice == 7:
		setName1 = input("Enter 1st set name : ")
		if setName1 in di.keys():
			setName2 = input("Enter 2nd set name : ")
			if setName2 in di.keys():
				ans = di[setName1].intersection(di[setName2])
				print(ans)
			else:
				print("Set name dNE..")
		else:
			print("Set name dNE..")
		pass
	# finding difference of 2 sets
	elif choice == 8:
		setName1 = input("Enter 1st set name : ")
		if setName1 in di.keys():
			setName2 = input("Enter 2nd set name : ")
			if setName2 in di.keys():
				ans = di[setName1].difference(di[setName2])
				print(ans)
			else:
				print("Set name dNE..")
		else:
			print("Set name dNE..")
		pass
	# finding symmetric difference between 2 sets
	elif choice == 9:
		setName1 = input("Enter 1st set name : ")
		if setName1 in di.keys():
			setName2 = input("Enter 2nd set name : ")
			if setName2 in di.keys():
				ans = di[setName1].difference(di[setName2])
				ans2 = di[setName2].difference(di[setName1])
				print(ans.union(ans2))
			else:
				print("Set name dNE..")
		else:
			print("Set name dNE..")
		pass
	# exit the program
	elif choice == 10:
		break
	else:
		print("Enter the correct choice.. ")
		pass