"""In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution.
 The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):


Local(L): Defined inside function/class
Enclosed(E): Defined inside enclosing functions(Nested function concept)
Global(G): Defined at the uppermost level
Built-in(B): Reserved names in Python builtin modules
"""

# Global Scope
from math import pi
pi = 'global pi variable'
def inner():
	pi = 'inner pi variable'
	print(pi)

inner()
print(pi)
