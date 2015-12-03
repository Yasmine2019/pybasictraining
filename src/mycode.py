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
	
def return_many(r1, r2, r3):
	return(r1 + 2, r2 + 2, r3 + 2)

r1, r2, r3 = return_many(1, 2, 3)

import some_library
from some_library import return_val

some_library.