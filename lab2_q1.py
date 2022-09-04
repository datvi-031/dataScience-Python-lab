# empty dictionary is created
di = {}

while 1:
	# select from contents
	print("\n1. >> Insert student record")
	print("2. >> Delete student record")
	print("3. >> Search in student records")
	print("4. >> Exit")
	choice = int(input("Select any option : "))

	# insert student record
	if choice == 1:
		li = []
		rollNo = input("Enter Student Roll number : ")
		li.append(input("Enter student name : "))
		li.append(input("Enter student CGPA : "))
		li.append(input("Enter student mobile no : "))
		di[rollNo] = li;
		pass

	# delete student record
	elif choice == 2:
		rollNo = input("Enter student rollNo : ")
		if rollNo in di.keys():
			di.pop(rollNo)
			print("Student record deleted successfully..")
		else:
			print("Student roll number dNE")
		pass

	# search in student record
	elif choice == 3:
		rollNo = input("Enter student rollNo : ")
		if rollNo in di.keys():
			print(di[rollNo])
		else:
			print("Student roll number dNE")
		pass

	# exit the program
	elif choice == 4:
		break
	else:
		print("Wrong choice try again : ")
		pass
	pass

print(li)