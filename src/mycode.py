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
	u = l[0]
	l.pop(l[0])
	l.append(u)
	return None
