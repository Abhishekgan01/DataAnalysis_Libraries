import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250) #normal - normal distribution, mean(average) - 170, standard deviation - 10, no of random no - 250
plt.hist(x)
plt.show()