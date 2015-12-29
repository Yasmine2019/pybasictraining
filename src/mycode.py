x = 3
print(x)
s = "I am a string"
print(s)
b = False
print(b)

def do_something(x1, x2):
	"""This does something"""
	return x1 * x2
	print("x1 * x2 = %d"%(x1 * x2))
  
def keyword_fn(keyword = None):
	if keyword == None:
		return "No"
	else:
		return keyword + 2
		
def return_many(x1, x2, x3):
	return(x1 + 2, x2 + 2, x3 + 2)
	
r1, r2, r3 = return_many(1, 2, 3)

import some_library
teapot = some_library.i_am_a_teapot()
def gonna_call_stuff(p):
	return some_library.multiply_by_2(p)

t1 = ()
t2 = (False, )
t3 = (None,) * 32000
t4 = ('foo', 1, False)
t5 = t4[0]

def measure_tuple(t):
	return len(t)


def sum_tuple(e):
	if len(e) == 5:
		return e[0] + e[1] + e[2] + e[3] + e[4]
	else:
		return None

l1 = []
l2 = [False, ]
l3 = [None,] * 32000
l4 = ['foo', 1, False]
l5 = l4[0]

def measure_list(t):
	return len(t)

def sum_list(e):
	if len(e) == 5:
		return e[0] + e[1] + e[2] + e[3] + e[4]
	else:
		return None

def wopit(l): 
	if len(l) != 0:
		l.append(l[0])

def bopit(l): 
	if len(l) != 0:
		l.pop(-1)

def mopit(l): 
	if len(l) != 0:
		l.pop(0)

def zopit(l):
	for x in range(len(l)):
		if l[x] == 'item' and x > 100:
			return True
	return False

d1 = {}
d2 = { 'k1' : 'item', 'k2' : (1, 2) }
d3 = d2['k2']

def superd(d):
	for key in range(1, 10001):
		value = '%s' % key
		d.update({key:value})


class MyClass:	

	clsvar = 3

	def __init__(self, instvar):
		self.instvar = instvar
		if self.instvar == 'Hi':
			self.instvar = 'Hello'

	def add5(self, a):
		self.instvar = self.instvar + a + 5
		if self.instvar > 100:
			return True
		else:
			return False

	@property
	def prop(self):
		return 'hi'

	@prop.setter
	def prop(self, value):
		self._prop = value

	def a(self, instvar1):
		self.instvar1 = instvar1

	def b(self):
		if (hasattr(self, "instvar1")):
			return self.instvar1
		else:
			return None


mine = MyClass('Hi')
mine2 = MyClass('Hi')
