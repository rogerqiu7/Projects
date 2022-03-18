import matplotlib.pyplot as plt
import numpy as np

# Law of Large Numbers:
# as a sample size grows, its mean gets closer to the average of the whole population.

def coin_flip_experiment():
  # defining our two coins as lists
  coin1 = ['Heads', 'Tails']
  coin2 = ['Heads', 'Tails']
 
  # "flipping" both coins randomly, np.random.choice picks random element from coin1 and 2
  coin1_result = np.random.choice(coin1)
  coin2_result = np.random.choice(coin2)
 
  # checking if both flips are heads
  if coin1_result == 'Heads' and coin2_result == 'Heads':
    return 1
  else:
    return 0
 
# how many times we run the experiment
num_trials = 1000
probability = []
flips = []
# keep track of the number of times heads pops up twice
two_heads_counter = 0
 
# perform the experiment X times
for flip in range(num_trials):
    
  # if both coins are heads, add 1 to the counter
  two_heads_counter += coin_flip_experiment()

  # keep track of the probability of two heads at each flip 
  probability.append(two_heads_counter/(flip+1))
  
  # keep a list for number of flips, goes until num_trail
  flips.append(flip+1)
 
# plot all flips and probability of two heads
plt.plot(flips, probability, label='Experimental Probability')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Two Heads')

plt.hlines(0.25, 0, num_trials, colors='orange', label='True Probability')
plt.legend()

plt.show()