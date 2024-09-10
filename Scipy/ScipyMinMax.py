from scipy.optimize import minimize

def eqn(x):
  return x*2 + x + 2
mymin = minimize(eqn, 100, method='BFGS')
print(mymin.x)