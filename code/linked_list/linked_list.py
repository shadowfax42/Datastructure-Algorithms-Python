class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1
	
	def append(self, value):
		new_node = Node(value)
		if self.head is None or self.length == 0: # check if the list is empty
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node # pointing to new node
			self.tail = new_node
		self.length += 1
		return True # this is not required but will be used by another method later on
	
	def print_list(self):
			temp = self.head
			while temp is not None:
					print(temp.value)
					temp = temp.next

	def pop(self):
		# when we have no nodes
		if self.length == 0:
			return None
		# when we have >= 2 nodes
		temp = pre = self.head
		while temp.next is not None: # same as while (temp.next)
			pre = temp
			temp = temp.next
		self.tail = pre
		self.tail.next = None
		self.length -= 1

		# when we have one node
		if self.length == 0:
			self.head = None
			self.tail = None
		return temp
	
	def prepend(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		self.length += 1
		return True

	def pop_first(self):
		# when we have no nodes
		if self.length == 0:
			return None
		# if we have >= 2 nodes
		temp = self.head # store the current head in a temp var
		self.head = self.head.next  # set current head to point to the next node
		temp.next = None # set temp to None
		self.length -= 1 # decrement the length
		# when we have one node
		if self.length == 0:
			self.tail = None
		return temp

	def get(self, index):
		if index < 0 or index >= self.length:
			return None
		temp = self.head
		for _ in range(index):
			temp = temp.next
		return temp

	def set_value(self, index, value):
		if index < 0 or index >= self.length:
			return None
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False
	
	def insert(self, index, value):
		if index < 0 or index >= self.length:
			return False
		if index == 0:
			return self.prepend(value)
		if index == self.length:
			return self.append(value)
		# create a new node
		new_node = Node(value)
		# get the head of the node before the specified index
		temp = self.get(index-1)
		new_node.next = temp.next # point pointer of new node to temp.next
		temp.next = new_node 
		self.length += 1
		return True
	
	def remove(self, index):
		if index < 0 or index >= self.length:
			return None
		if index == 0:
			return self.pop_first()
		if index == self.length - 1:
			return self.pop()
		
		prev = self.get(index - 1)
		# temp = self.get(index) # cant use this because get() is O(n)
		temp = prev.next
		prev.next =  temp.next
		temp.next = None
		self.length -= 1
		return temp
	
	def reverse(self):

		temp = self.head
		# reverse head and tail
		self.head, self.tail = self.tail, temp





# TESTING
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()
print("*******************************")
my_linked_list.set_value(2, 100000)
my_linked_list.print_list()
print("*******************************")
my_linked_list.insert(0, 13)
my_linked_list.print_list()

print("*******************************")
my_linked_list.remove(2)
my_linked_list.print_list()
# my_linked_list.prepend(0)
# print("\n----------------adding a node with 400 at the beginning--------------------")
# my_linked_list.print_list()

# my_linked_list.pop_first()
# print("\n----------------Pop First (1)--------------------")
# my_linked_list.print_list()

# my_linked_list.pop_first()
# print("\n----------------Pop First (2)--------------------")
# my_linked_list.print_list()

# print(my_linked_list.pop_first())
# print("\n----------------Pop First (3)--------------------")
# my_linked_list.print_list()


# my_linked_list.pop()
# print("\n----------------Popping when we have zero items--------------------")
# my_linked_list.print_list()

# my_linked_list.pop()
# print("\n----------------Popping when we have zero items--------------------")
# my_linked_list.print_list()

# my_linked_list.prepend(500)
# print("\n----------------adding a node with 400 at the beginning--------------------")
# my_linked_list.print_list()