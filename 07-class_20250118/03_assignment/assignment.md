# Create a Word Guessing Game

1. Create a word guessing game. 
2. The computer will guess a number.  
- Use python package `random` to generate a random number. 
```python
import random

random_number = random.randInt(1,5) # will generate a random number from specified range

```

or use 

```python

from random import randint

random_number = randint(1,5)

```

3. The game should keep running until user guesses the number. Use `while` function.

4. Keep the track of user tries. When user guess the number, show the number of tries being used to guess the number. 