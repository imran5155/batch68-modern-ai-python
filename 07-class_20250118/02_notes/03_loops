## The Problem:

Imagine you’re organizing a birthday party and you want to send an invitation message to 50 of your friends. Without any tools or shortcuts, you would have to write the same message 50 times, changing only the name of each friend. This is repetitive and time-consuming.

you would have to manually send each message like this:

```
print("Hi Alice, you’re invited to my birthday party!")
print("Hi Bob, you’re invited to my birthday party!")
print("Hi Charlie, you’re invited to my birthday party!")
# ...and so on, for 50 friends
```

If you have a long list of friends, this approach quickly becomes impractical. Not only does it take a lot of time, but if you want to change the message later, you’d have to edit each line individually.

## The Solution: Using Loops to Automate Invitations

Now, let’s say you want to automate this process. You can use a loop to send the same message to all your friends with just a few lines of code

```
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]  # and so on, up to 50 names

for friend in friends:
    print(f"Hi {friend}, you’re invited to my birthday party!")

```

---
# For Loop

The for loop is used to iterate over a sequence (like a list, tuple, set, or string) or any other iterable object. It allows you to execute a block of code a specific number of times, usually determined by the length of the sequence or the range of values.

### Syntax

```
for item in iterable:
    # Execute this block of code
```

### Iterating over a list

```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Iterating over a string

```
for letter in "Python":
    print(letter)
```

### Using range() in a for loop

```
for i in range(5):
    print(i)
```

### Specifying a start and end in range()

```
for i in range(2, 6):
    print(i)
```

### Using a step in range()

```
for i in range(1, 10, 2):
    print(i)
```

### for Loop with zip()
Iterating over two lists simultaneously

```
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

---

# Nested for Loops

Nested for loops are used when you need to perform an action that involves iterating over multiple sequences or when dealing with multi-dimensional data (like a matrix or list of lists).


### Iterating over a list of lists

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

---


## Python provides some statements to control the flow of loops:

The continue and break statements are control flow tools in Python that allow you to alter the behavior of loops (for and while loops). They provide ways to skip iterations or exit loops prematurely based on specific conditions.

### 1. break Statement

The break statement is used to exit a loop immediately, regardless of the loop’s condition. When break is encountered, the loop terminates, and the program continues with the next statement after the loop.

***Use in a for Loop***

```
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
```

***Use in a while Loop***

```
count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break  # Exit the loop when count is 5
```


### 2. continue Statement

The continue statement is used to skip the current iteration of a loop and proceed with the next iteration. When continue is encountered, the loop doesn’t terminate; it just skips the remaining code in the current iteration and moves on to the next iteration.

***Use in a for Loop***
```
for i in range(1, 6):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)

```

***Use in a while Loop***

```
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop when count is 3
    print(count)
```


When to Use break and continue:

	•	break:
	•	Exiting a loop when a certain condition is met (e.g., finding an item in a list and stopping further search).
	•	Preventing infinite loops when a certain condition occurs.
	•	continue:
	•	Skipping certain values in a loop (e.g., skipping over unwanted data or values that don’t need processing).
	•	Avoiding unnecessary computations or actions within specific loop iterations.


Both break and continue are powerful tools for managing the flow of loops, allowing you to fine-tune how and when specific blocks of code are executed.

---
# The While Loop:

```json
while you have peanuts
    keep eating
```
- `while` and `if` both checks the conditions. If the condition is met (`True`), the instructions in `if` block exeuctures only once. However, in `while`, if the condition is met (`True`), the instructions in the `while` block runs more than once. 

- If condition evaluates to `False` the instuctions in the block never runs. 

- There should be a mechanism in the body to change the condition value. Otherwise the body will keep executing forever. 

## Situation
You have a class that runs until 6 PM. During this time, you want to keep learn Python. You don’t want to stop coding until the clock hits 6 PM.


In a real-life scenario, you might keep checking the time every few minutes while you’re coding to see if it’s 6 PM yet:

	1.	Start coding.
	2.	Check the time.
	3.	If it’s not 6 PM, continue coding.
	4.	Repeat this process until it’s 6 PM.

This approach works, but it requires constant attention to the clock, which can be distracting.

# While Loop
The while loop in Python is a control flow statement that allows code to be executed repeatedly based on a given condition. The loop continues to execute as long as the condition evaluates to True. Once the condition becomes False, the loop stops running.

#### syntax
```
while condition:
    # Code block to be executed repeatedly
```

In a programming context, you can automate this process using a while loop that will allow you to keep coding until the time reaches 6 PM.

```
while current_time < 18:  # 18 represents 6 PM in 24-hour format
    print("Still coding... The time is not yet 6 PM.")

print("It's 6 PM! Time to stop coding and end the class.")
```

---

### Example 1: Basic while Loop

```
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```
Explanation:

	•	The loop starts with count equal to 0.
	•	It prints the value of count and then increments count by 1.
	•	This process repeats until count is no longer less than 5.


### Example 2: while Loop with a Condition
You can use a while loop to keep prompting the user until they enter a valid input.

```
password = ""
while password != "Pass123":
    password = input("Enter the password: ")

print("Access granted")
```


### Example 3: Infinite while Loop
A while loop can run indefinitely if the condition never becomes False. This is known as an infinite loop, and it will continue to run until you manually stop it or break out of it with a break statement.

```
while True:
    print("This loop will run forever")
    # You can include a break condition to exit the loop
```

***Note: Be careful with infinite loops, as they can cause your program to hang if not properly managed.***


