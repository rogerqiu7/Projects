# Law of Large Numbers - Use of hypothesis testing functions to build visualizations in proving the Law of Large numbers
# Law: the average of the results obtained from a large number of trials should be close to the expected value and as more trials are performed
# as a sample size of a coin flip grows, its average of heads/tails gets closer to the true proability of 50%:
# therefore the probability of 2 heads in a row should be 25%, 

import matplotlib.pyplot as plt
import numpy as np

# create function that flips 2 coins randomly and returns 1 if both coins show head
def coin_flip_experiment():
  # defining our two coins as lists
  coin1 = ['Heads', 'Tails']
  coin2 = ['Heads', 'Tails']
 
  # "flipping" both coins randomly, np.random.choice picks random element (heads or tails) from coin1 and coin2
  coin1_result = np.random.choice(coin1)
  coin2_result = np.random.choice(coin2)
 
  # checking if both flips are heads, return 1 if it is
  if coin1_result == 'Heads' and coin2_result == 'Heads':
    return 1
  else:
    return 0
 

# how many times we run the experiment
num_trials = 1000
# keeps track of the probability of two heads at each flip, should get closer to true probability of 0.25
probability = []
# keeps track of number of trails ran
flips = []
# keep track of the number of times heads pops up twice
two_heads_counter = 0
 
# perform the experiment X times
for flip in range(num_trials):
    
  # if both coins are heads, add 1 to the counter
  two_heads_counter += coin_flip_experiment()

  # counter / number of times flipped = probability of two heads so far, append each updated probability to list
  probability.append(two_heads_counter/(flip+1))
  
  # keep a list for number of flips, goes until num_trail (1000)
  flips.append(flip+1)
 
# plot all flips and probability of two heads
plt.plot(flips, probability, label='Experimental Probability')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Two Heads')

plt.hlines(0.25, 0, num_trials, colors='orange', label='True Probability')
plt.legend()

plt.show()