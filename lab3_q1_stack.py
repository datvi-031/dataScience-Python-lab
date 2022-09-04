# STACK USING LINKED LIST
class node:
	# creation of node for using in linked list
	def __init__(self, item):
		self.data = item
		self.next = None

class stack:
	# to keep track of no of elements in linkedList
	cnt = 0
	def __init__(self, size):
		self.head = None
		self.size = size

	# insert element at beginning of linkedList
	def push(self, item):
		# if size of stack is 0, then head node is created with item
		if self.cnt == 0:
			self.head = node(item)
			print(">> Data : "+str(item)+"\toperation [INSERTION] : status [ACCEPTED]")
			self.cnt+=1
			return

		if(self.cnt == self.size):
			print(">> Data : " +str(item) + "\toperation [INSERTION] : status [STACK OVERFLOW]")
			return

		new = node(item)
		new.next = self.head
		self.head = new
		self.cnt+=1
		print(">> Data : " +str(item)+"\toperation [INSERTION] : status [ACCEPTED]")

	# delete element at begininng of linkedList
	def pop(self):
		if(self.cnt == 0):
			eMsg = "operation [POP] : status [STACK UNDERFLOW]"
			return eMsg

		temp = self.head
		popVal = self.head.data
		self.head = self.head.next
		temp = None
		self.cnt-=1
		return popVal

	def peek(self):
		if self.head == None:
			eMsg = "operation [PEEK] : status [STACK UNDERFLOW]"
			return eMsg

		return self.head.data

	# printing contents of the stack
	def printStack(self):
		tempHead = self.head
		print("(Contents of stack : ", end=" ")
		while tempHead!=None :
			print(tempHead.data, end=" ")
			tempHead = tempHead.next
		print(")")


# stack of size 5 is declared
stk = stack(5)

stk.push(12)
stk.push(23)
stk.push(44)
stk.push(55)
stk.push(41)
stk.printStack()
stk.push(88)

print(" >> popped value : ",stk.pop())
stk.printStack()
print(" >> popped value : ",stk.pop())
print(" >> popped value : ",stk.pop())
print(" >> peek value : ",stk.peek())
print(" >> popped value : ",stk.pop())
stk.push(818)
stk.printStack()
print(" >> popped value : ",stk.pop())
print(" >> popped value : ",stk.pop())
print(" >> peek value : ",stk.peek())
print(" >> popped value : ",stk.pop())
print(" >> peek value : ",stk.peek())
stk.printStack()