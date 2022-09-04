# library management system

import pickle
li = ["b_name", "acc_no", "title", "price", "edition", "year", "Author"]

def writeFile(n):
	print("")
	file = open("data.dat", "ab")	
	for x in range(1,n+1):
		l = list()
		print("BOOK {}:".format(x))
		l.append(input(">> Enter book name: "))
		l.append(input(">> Enter acc number: "))
		l.append(input(">> Enter title of book: "))
		l.append(input(">> Enter book price: "))
		l.append(input(">> Enter edition: "))
		l.append(input(">> Enter year: "))
		l.append(input(">> Enter Author name: "))
		print("")
		pickle.dump(l, file)
		l.clear()
	file.close()

def filecheck():
	try:
		file = open("data.dat", "rb")
		return True
	except FileNotFoundError:
		print("file DOESNOT EXISTS")
		return False

def readFile(li):
	print("")
	if(filecheck()):
		file = open("data.dat","rb")
		readData = 1
		while True:
			try:
				readData = pickle.load(file)
				for x in range(0,len(readData)):
					print(">> {} : {}\n".format(li[x],readData[x]), end="\t")
				print("")
			except EOFError:
				break
		file.close()
		print("")

def searchBook(book, li):
	print("")
	file = open("data.dat", "rb")
	if(filecheck()):
		while True:
			try:
				readData = pickle.load(file)
				if book == readData[2]:
					print("BOOK FOUND:")
					for x in range(0, len(readData)):
						print(">> {} : {}\n".format(li[x],readData[x]), end="\t")
					print("")
					return
			except EOFError:
				break
		print(">> BOOK DOESNOT EXISTS IN THE FILE")
		print("")
	file.close()

while True:
	print("1. Enter n-book information [write]")
	print("2. Get All-book information [read]")
	print("3. Search for a book based on book title [search]")
	print("4. Exit")
	chc = int(input("Enter your choice: "))

	if chc == 1:
		n = int(input("Enter no of books [to be dumped]: "))
		writeFile(n)
	elif chc == 2:
		readFile(li)
	elif chc == 3:
		book = input("\n>> Enter the book title: ")
		searchBook(book, li)
	elif chc == 4:
		break
	else:
		print("[Please enter valid option.] try again... ")