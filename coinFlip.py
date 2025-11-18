```python
# Import the random module to generate random numbers
import random

# Initialize a counter variable to keep track of the number of times heads comes up
heads = 0

# Loop 1000 times to simulate 1000 coin flips
for i in range(1, 1001):
    # Generate a random number (0 or 1) to simulate a coin flip
    if random.randint(0, 1) == 1:
        # If the number is 1, increment the heads counter
        heads = heads + 1
    
    # Print a message to indicate we've reached the halfway point
    if i == 500:
        print('Halfway done!')

# Print the final count of times heads came up
print('Heads came up ' + str(heads) + ' times.')
```