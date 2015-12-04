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
