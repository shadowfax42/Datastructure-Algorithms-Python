## Big O

- Big O is a way of comparing code mathematically (how efficient it's running)
- Time complexity is measured in the number of operations that it takes to complete something
- Space complexity: the space in memory a chunk of code takes
---
- **Time complexity:** How much time is needed to run an algorithm.
- **Space Complexity:** How much space is needed to run an algorithm.

### Symbols
- Omega $\Omega$
- Theta $\theta$
- Omicron $\mathcal{O}$

### Terminology
- The best case scenario for running a piece of code, that is Omega $\Omega$
- the average case is theta  $\theta$
- And worst case is Omicron or  $\mathcal{O}$

**==When talking about big O, we are always talking about worst-case**

### Big $\mathcal{O}$: $\mathcal{O}(n)$

```python
def print_items(n):
	for i in range(n):
		print(i)
print_items(10)
```

- This is an example of $\mathcal{O}(n)$. whatever $n$ was, that was the number of operations.
- $\mathcal{O}(n)$ is always going to be a straight line
	- It is what is called **Proportional**

### Big $\mathcal{O}$: Drop Constants

```python
def print_items(n):
	# first for loop
	for i in range(n):
		print(i)
	# second for lopp
	for j in range(n):
		print(j)
print_items(10)
```

- This piece of code ran in $n + n = 2n$ times
- So it doesn't matter if it's $\mathcal{O}(2n)$ $\mathcal{O}(10n)$, or $\mathcal{O}(100n)$, we drop the constant and we just write it as $\mathcal{O}(n)$.

### Big $\mathcal{O}$: $\mathcal{O}(n^2)$

```python
def print_items(n):
	for i in range(n):
		for j in range(n)
			print(i, j)
print_items(10)
```

- This piece of code ran in $n\times n = n^2$ $\rightarrow \mathcal{O}(n^2)$ 

![[Pasted image 20230605123911.png]]

- So from the graph, we see that $\mathcal{O}(n^2)$  is much steeper than $\mathcal{O}(n)$, and this means it's a lot less efficient from a time complexity standpoint than that of $\mathcal{O}(n)$ 

### Big $\mathcal{O}$: Drop Non-Dominants

```python
def print_items(n):
	# first for loop (O (n^2))
	for i in range(n):
		for j in range(n):
			print(i, j)
			
	# second for loop (O(n))
	for k in range(n):
		print(k)
		
print_items(10)
```

- First loop ran in $\mathcal{O}(n^2)$, while the second loop ran in $\mathcal{O}(n)$. 
- We can write this as $\mathcal{O}(n^2 + n)$
- So in this equation, $n^2$ is the dominant term and that stand alone $n$ is the non-dominant term. So, we drop the non-dominant

### Big $\mathcal{O}$: $\mathcal{O}(1)$

```python
def add_items(n):
	return n + n
```

- In this case, we only have one operation (addition). Even if $n$ gets bigger, we still have operation, hence it's $\mathcal{O}(1)$

- $\mathcal{O}(1)$ is called Constant time (most efficient Big  $\mathcal{O}$)

### Big $\mathcal{O}$: $\mathcal{O}(\log n)$

![[Pasted image 20230605125545.png]]
![[Pasted image 20230605125651.png]]

### Big $\mathcal{O}$: Different Terms for Inputs

```python
def print_items(a, b):
	
	for i in range(a): # O(a)
		print(i)
	for j in range(b): # O(b)
		print(j)
```

- You can't use $n$ here. We have to use $a$ and $b$
- $\mathcal{O}(a) + \mathcal{O}(b) = \mathcal{O}(a + b)$

```python
def print_items(a, b):
	
	for i in range(a): #
		print(i)
		for j in range(b):
			print(i, j)
```

- $\mathcal{O}(a) \times \mathcal{O}(b) = \mathcal{O}(a \times b)$

### Big $\mathcal{O}$ of Lists

- Removing or adding from the end of the list is $\mathcal{O} (1)$ 
- Removing or adding from the start of a list is $\mathcal{O}(n)$ because you have to re-index the whole list
- Same applies to the middle. you still have to index the remaining elements in the list

### Recap
- $\mathcal{O}(n^2)$: Loop within a loop
- $\mathcal{O}(n)$: Proportional
- $\mathcal{O}(\log n)$: Divide and Conquer
- $\mathcal{O}(1)$ Constant

[Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell (bigocheatsheet.com)](https://www.bigocheatsheet.com/)
