class Node:
	def __init__(self,val):
		self.val = val
		self.next = None


class LinkList:
	def __init__(self,):
		self.head = None
		self.count = 0

	def size(self):
		return self.count

	def empty(self):
		return self.size() == 0


	def value_at(self, index):
		ptr = self.head
		if index < self.count:
			while index:
				ptr = ptr.next
				index -= 1
			return ptr.val
		else:
			raise Exception("index out of range")


	def push_front(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		self.count += 1
		return

	def pop_front(self):
		if self.count >= 1:
			node = self.head
			self.head.next = self.head
			self.count -= 1
			return node 
		else:
			raise Exception("Nothing to pop")

	def find_back(self):#return last node
	    if self.count >= 1:
			ptr = self.head
			while ptr.next:
				ptr = ptr.next
			return ptr
		else:
			return None

	def push_back(self, val):
		if self.count == 0:
			self.push_front(val)
		else:
			last_node = self.find_back()
			last_node.next = Node(val)
		    self.count += 1

	def front(self):
		if self.count > 0:
			return self.head.val
		else:
			return None

	def back(self):
		if self.count > 0:
			return self.find_back().val
		else:
			return None

	def insert(self,index, value):
		ptr = self.head
		if index < self.count:
			while index > 0:
				ptr = ptr.next
				index -= 1
			temp = ptr.next
			ptr.next = Node(value)
			ptr.next.next = temp
			self.count += 1

		else:
			raise Exception("index out of bound")

	def erase(self,index):
		ptr = self.head
		if index == 0:
			self.pop_front()
		elif index < self.count:
			while index > 1:
				ptr = ptr.next
				index -= 1
			ptr.next = ptr.next.next
			self.count -= 1
		else:
			raise Exception("index out of bound")

	def value_n_from_end(self, n):
		if n > self.count:
			front_pointer = self.head
			ptr = self.head
			while n:
				front_pointer = front_pointer.next
			while front_pointer.next:
				front_pointer = front_pointer.next
				ptr = ptr.next
			return ptr.val
		else:
			raise Exception("n is too large")

	def reverse(self):
		#A->B->C
		#A<-B<-C
		if self.count == 1:
			return # nothing to reverse
		ptr = self.head.next
		prev_ptr = self.head
		while ptr:
			next_ptr = ptr.next
			ptr.next = prev_ptr

			prev_ptr = ptr
			ptr = next_ptr

	def remove_value(self,value):
		ptr = self.head
		prev_ptr = Node(0)
		dummy_head = prev_ptr
		prev_ptr.next = ptr
		while ptr:
			if ptr.val == value:
				prev_ptr.next = ptr.next
				self.count -= 1
				break
			prev_ptr = prev_ptr.next
			ptr = ptr.next
		self.head = dummy_head.next










