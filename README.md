# coinFlip.py

**Coin Flip Simulator**

This Python script simulates 1000 coin flips and calculates the number of times heads comes up. Here's a breakdown of the code:

**Importing the `random` module**

The script starts by importing the `random` module, which provides functionality for generating random numbers.

**Initializing the counter variable**

A counter variable `heads` is initialized to 0, which will keep track of the number of times heads comes up during the simulation.

**Simulating 1000 coin flips**

The script uses a `for` loop to iterate 1000 times, simulating 1000 coin flips. Each iteration represents a single coin flip.

**Generating a random number**

Inside the loop, a random number (0 or 1) is generated using `random.randint(0, 1)`. This simulates a coin flip, where 0 represents tails and 1 represents heads.

**Incrementing the counter**

If the generated random number is 1 (