import random
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

num_runs = 1000
num_experiment = 100000
def flip_coin(flip_amt):
    total = 0
    choices = [0, 1]
    for x in range (flip_amt):
        total += random.choice(choices)
    return total
def roll_dice(roll_amt):
    total = 0
    choices = [1,2,3,4,5,6]
    for x in range (roll_amt):
        total += random.choice(choices)
    return total
S = [0]*num_experiment
for x in range (len(S)):
    S[x] = roll_dice(num_runs)
xmin = min(S)
xmax = max(S)
plt.hist(S,np.arange(xmin, xmax+1,step=1))
temp1, temp2, ymin, ymax = plt.axis()
bin_width = (temp2 - temp1)/(num_runs *(temp2 - temp1)/num_runs)
plt.xticks(np.arange(xmin, xmax+1,step=10))
plt.yticks(np.arange(ymin, ymax+10, step=100))
y = np.linspace(xmin, xmax, 1000)
plt.plot(y, stats.norm.pdf(y, loc=np.mean(S), scale=np.std(S)) * num_experiment * bin_width)
plt.title("Rolling " + str(num_runs) + " die " + str(num_experiment) + " times")
plt.xlabel("Sum of " + str(num_runs) + " rolls")
plt.ylabel("Occurances")
plt.show() 