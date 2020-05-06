import numpy as np

random1 = np.random.uniform(size=100)
print(random1)
random2 = np.random.uniform(size=100)
print(random2)

random1means = np.mean(random1)
print(random1means)
random2means = np.mean(random2)
print(random2means)

from matplotlib import pyplot as plt

plt.plot(random1, label = 'random number 1')
plt.title('random number 1')
plt.show()

plt.plot(random2, label = "random number 2")
plt.title("random number 2")
plt.show()

random3 = (np.add(random1, random2))/2
print(random3)
random3means = np.mean(random3)

plt.plot(random3, label = "random number 3")
plt.title("random number 3")
plt.show()