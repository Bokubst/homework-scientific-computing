import numpy as np

random1 = np.random.uniform(size=100)
print("random1 values")
print(random1 , "\n")

random2 = np.random.uniform(size=100)
print("random2 values")
print(random2 , "\n")

from matplotlib import pyplot as plt

plt.plot(random1, label = 'random number 1')
plt.title('random number 1')
ran_mean1 = [np.mean(random1) for i in random1]
plt.plot(ran_mean1, label = 'mean value')
plt.show()

plt.plot(random2, label = "random number 2")
plt.title("random number 2")
ran_mean2 = [np.mean(random2) for i in random2]
plt.plot(ran_mean2, label = 'mean value')
plt.show()

random3 = (np.add(random1, random2))/2
print("random3 values")
print(random3)
random3means = np.mean(random3)

plt.plot(random3, label = "random number 3")
plt.title("random number 3")
ran_mean3 = [np.mean(random3) for i in random3]
plt.plot(ran_mean3, label = 'mean value')
plt.show()

random1means = np.mean(random1)
print("mean of random1")
print(random1means  , "\n")

random2means = np.mean(random2)
print("mean of random2")
print(random2means  , "\n")

random3means = np.mean(random3)
print("mean of random3")
print(random3means)