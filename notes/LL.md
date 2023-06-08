
## Linked List

### Intro

#### Differences between a linked list and a list

- Linked list doesn't have indexes
- A list is in a contiguous place in memory (all right next to each other in memory)
- With a linked list, all of the nodes are spread out all over the place
- with a linked list, we have a variable called `Head` and it points to the first node in the list. It also has a variable called `Tail` which points to the last item, and then each node points to the next. The last node points to `None`

### LL: Big $\mathcal{O}$

![[Pasted image 20230605151452.png]]

### LL: Under the hood

![[Pasted image 20230605151930.png]]
is equivalent to

![[Pasted image 20230605151908.png]]

### LL: Constructor

```python
class LinkedList:
	def __init__(self, value):
	# Create New Node
	# Initialize the LL

	def append(self, value):
	# Create New Node
	# Add Node to the end

	def prepend(self, value):
	# Create New Node
	# Add Node to begining

	def insert(self, index, value):
	# Create New Node
	# insert Node

```

- So, we don't want to write code for creating a new node 4 different times
- We are going to create a class that does nothing but create nodes

```python
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

my_linked_list = LinkedList(4)
print(my_linked_list.head.value) # 4
```

![[Pasted image 20230605153306.png]]

```python
def print_list(self):
	temp = self.head
	while temp is not None:
		print(temp.value)
		temp = temp.next
```

```python
def append(self, value):
	new_node = Node(value)
	if self.head is None: # check if the list is empty
		self.head = new_node
		self.tail = new_node
	else:
		self.tail.next = new_node # pointing to new node
		self.tail = new_node
	self.length += 1
	return True # this is not required but will be used by another method later on
```

### POP

to pop a node, we will need to traverse the whole linked list until we read the node we need to remove

- We have two edge cases:
	- The first edge case is if we have an empty link list.
	- And then the other edge case is if we only have one node in the list.