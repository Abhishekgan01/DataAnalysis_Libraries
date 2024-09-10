from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)
myroot = root(eqn, 100)
print(myroot.x)
print(myroot)