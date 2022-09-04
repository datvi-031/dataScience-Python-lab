# QUEUE USING LINKED LIST
class node:
	# creation of node for using in linked list
	def __init__(self, item):
		self.data = item
		self.next = None

class queue:
	# to keep track of no of elements in linkedList
	cnt = 0
	def __init__(self, size):
		self.head = None
		self.size = size

	# insert element at end of linkedList
	def enqueue(self, item):
		# if size of queue is 0, then head node is created with item
		if self.cnt == 0:
			self.head = node(item)
			print(">> Data : "+str(item)+"\toperation [INSERTION] : status [ACCEPTED]")
			self.cnt+=1
			return

		if(self.cnt == self.size):
			print(">> Data : "+str(item) + "\toperation [INSERTION] : status [QUEUE OVERFLOW]")
			return

		tempHead = self.head
		while(tempHead.next != None):
			tempHead=tempHead.next
		new = node(item)
		tempHead.next = new
		new.next = None
		print(">> Data : "+str(item)+"\toperation [INSERTION] : status [ACCEPTED]")
		self.cnt+=1

	# delete element at begininng of linkedList
	def dequeue(self):
		if(self.cnt == 0):
			eMsg = "operation [DEQUEUE] : status [QUEUE UNDERFLOW]"
			return eMsg

		temp = self.head
		popVal = self.head.data
		self.head = self.head.next
		temp = None
		self.cnt-=1
		return popVal

	# printing contents of the queue
	def printQueue(self):
		tempHead = self.head
		print("(Contents of queue : ", end=" ")
		while tempHead!=None :
			print(tempHead.data, end=" ")
			tempHead = tempHead.next
		print(")")

# queue of size 5 is declared
q = queue(5)

# declared head node as q
q.enqueue(22)
q.enqueue(34)
q.enqueue(9)
q.enqueue(21)
q.enqueue(11)
q.enqueue(4)
q.printQueue()
print(">> dequeued value : ", q.dequeue())
print(">> dequeued value : ", q.dequeue())
print(">> dequeued value : ", q.dequeue())
print(">> dequeued value : ", q.dequeue())
q.printQueue()
print(">> dequeued value : ", q.dequeue())
print(">> dequeued value : ", q.dequeue())
q.printQueue()