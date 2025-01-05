# Notes

## 1.  Mutable and Immutable data types
Mutable data types are those that can be changed after they are created. Immutable data types are those that cannot be changed after they are created.

- Immutable data types: `int`, `float`, `str`, `bool`
- Mutable data types: `list`, `set`, `dict`

-------------------

## 2.  `type`, `dir`, `id` builtin functions
- `type` provides the type of a variable
- `dir` provides the list of attributes and methods of a variable
- `id` provides the memory address of a variable

```python
w = True
x = 5
y = 3.0
z = "Hello"

print(type(w)) 
print(type(x))  
print(type(y))  
print(type(z))  

print(dir(w))  
print(dir(x)) 
print(dir(y))
print(dir(z))

print(id(w))  
print(id(x)) 
print(id(y))
print(id(z))
```
-------------------

## 3. Nested Lists

Imagine you are a teacher managing a classroom. You have a list of students, and for each student, you want to keep track of their grades in three different subjects: Math, Science, and English. You decide to use a nested list where each sublist represents a student, and within each sublist, you store the student’s name and their grades for the three subjects.

```
classroom = [
    ["Rehan", [85, 90, 88]],   # Rehan's grades: Math, Science, English
    ["Muzhar", [78, 85, 82]],  # Muzhar's grades: Math, Science, English
    ["Ibtisam", [92, 88, 91]], # Ibtisam's grades: Math, Science, English
    ["Usman", [60, 59, 65]]    # Usman's grades: Math, Science, English
]
```

In this nested list:

	•	The outer list represents the entire classroom, with each sublist representing a student.
	•	Each student’s sublist contains their name and another sublist of their grades in Math, Science, and English.


#### Accessing Specific Grades
***Rehan’s Science Grade:***

```
rehan_science_grade = classroom[0][1][1]
print(rehan_science_grade)  # Output: 90
```

***Usman’s English Grade:***
```
usman_english_grade = classroom[3][1][2]
print(usman_english_grade)  # Output: 65
```

#### Modifying a Student’s Grades
***Update Muzhar’s Math Grade:***
```
classroom[1][1][0] = 83
print(classroom[1])  # Output: ['Muzhar', [83, 85, 82]]
```

-------------------

## 4. Comparison Operators
Compare two values and return a Boolean result (True or False).

- Equal to: ==
- Not equal to: !=
- Greater than: >
- Less than: <
- Greater than or equal to: >=
- Less than or equal to: <=

```python 
result_equal: bool = 5 == 5
result_not_equal: bool = 10 != 7
result_greater_than: bool = 8 > 3
result_less_than: bool = 6 < 9
result_greater_equal: bool = 5 >= 5
result_less_equal: bool = 3 <= 4
```

Strings can be compared using comparison operators.
```python
str1 = "Hello"
str2 = "World"
print(str1 == str2)  # Output: False
print(str1 != str2)  # Output: True
print(str1 < str2)   # Output: True (since "H" comes before "W" lexicographically)
```
-------------------

## 5. Control Flows if-elif-else Statements

### The Problem: Making Decisions in Code

Imagine we're building a simple app that recommends activities based on the weather. On a sunny day, we want to suggest going for a walk, while on a rainy day, we'd suggest staying indoors and reading a book. But what if it's cloudy or snowing? How do we make our app smart enough to handle these different scenarios?

Without a way to make decisions, our app would always suggest the same thing, no matter the weather. This is where we hit our first roadblock as budding programmers: **How do we make our code choose the right path?**

### The Solution: conditional statements in Python

Python, like any language, needs a way to handle different situations. This is where **conditional statements** come into play. These are the structures that allow our code to decide what to do next based on certain conditions. In Python, we use `if`, `elif`, and `else` to guide these decisions.

#### The Story of Choices: `if`, `elif`, and `else`

Let’s dive into the story of how Python makes decisions.

1. **The `if` Statement**:

   - Think of `if` as the gatekeeper. It checks a condition and decides if the code block that follows should run.
   - For example: If the weather is sunny, the gatekeeper will open the door to the "go for a walk" suggestion.

   ```python
   weather : str = "sunny"

   if weather == "sunny":
       print("It's a beautiful day! Go for a walk.")
   ```

   We can also use `else` statement in above exmple.

   - For example: We want to specify something else is done if our condition is not met, then we use `else` statement.

   ```python
   weather : str = "sunny"

   if weather == "sunny":
       print("It's a beautiful day! Go for a walk.")
   else:
       print("Read the book")
   ```

   **Ternary Operator (Optional):**

   - Python offers another way to write the `if` `else` code with less number of lines i.e. **Ternary Operator**. Let's see how can we use Ternary Operator to write the same code.

   ```python
   # We can also write the above example like so.
   weather : str =  "sunny"

   if weather == "sunny":
       message : str = "It's a beautiful day! Go for a walk."
   else:
       message : str = "Read the Book"
   print(message)
   ```

   Nothing is changed so far, we just refactored the code. Also note, we've used ternary operator yet but we made a ground for understanding ternary operator.

   **_Use of Ternary Operator_**

   ```python
   weather : str == "sunny"
   message : str = "It's a beautiful day! Go for a walk." if weather == "sunny" else "Read the book"
   print(message)
   ```

   - By using ternary operator, we write the `if` `else` block in a single line.
   - Ealier, we wrote 5 lines of code for first example and 6 lines of code for second example.
   - With ternary operator, we just wrote 3 lines of code which provided the same result.

2. **The `elif` Statement**:

   - What if we've multiple choices, how do we make the decision then?
   - What if the weather isn’t sunny? That’s where `elif` (short for "else if") comes in. It's the gatekeeper’s assistant, ready to check another condition if the first one fails.
   - For example: If the weather is not sunny but cloudy, the assistant will suggest taking an umbrella just in case.

   ```python
   weather : str = "cloudy"

   if weather == "sunny":
       print("It's a beautiful day! Go for a walk.")
   elif weather == "cloudy":
       print("It might rain. Better take an umbrella.")
   ```

3. **The `else` Statement**:

   - Finally, there’s `else`, the last resort. If all other conditions fail, `else` steps in to provide a default action.
   - For example: If the weather isn’t sunny or cloudy, and perhaps it’s raining or snowing, `else` will suggest a cozy indoor activity.

   ```python
   weather : str = "rainy"

   if weather == "sunny":
       print("It's a beautiful day! Go for a walk.")
   elif weather == "cloudy":
       print("It might rain. Better take an umbrella.")
   else:
       print("Stay indoors and read a book.")
   ```

### Nested Conditional Statements

refer to onsite class code.

### Why It Matters

By using `if`, `elif`, and `else`, we give our program the power to make decisions just like we do in real life. This makes our code dynamic, flexible, and smart enough to handle different situations.

With conditional statements, we can solve problems like:

- **Customizing user experiences**: Show different messages or suggestions based on user input or external factors.
- **Automating tasks**: Only perform certain actions when specific conditions are met.
- **Creating complex algorithms**: Make our programs more sophisticated by handling multiple scenarios with ease.

### Examples

Here are some real-world examples that demonstrate the use of `if`, `elif`, nested `if`, and multiple `if` conditions in Python.

#### 1. Simple `if` Statement

**Scenario**: A user wants to check if they have enough balance to make a purchase.

```python
balance : int = 150
price : int = 100

if balance >= price:
    print("Purchase successful!")
```

**Explanation**: The `if` statement checks if the user's balance is greater than or equal to the price. If true, the purchase is successful.

#### 2. `if`-`elif`-`else` Chain

**Scenario**: A system that grades students based on their score.

```python
score : int = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**Explanation**: The program checks the score against several conditions using `if` and `elif`. If none of the conditions match, the `else` block runs, assigning an "F" grade.

#### 3. Nested `if` Statement

**Scenario**: A store offers a discount only to members who have also made purchases above a certain amount.

```python
is_member : bool = True
purchase_amount : int = 250

if is_member:
    if purchase_amount > 200:
        print("You are eligible for a 10% discount!")
    else:
        print("Spend more than $200 to get a discount.")
else:
    print("Become a member to enjoy discounts.")
```

**Explanation**: The first `if` checks if the user is a member. If true, it checks if their purchase amount exceeds $200 using a nested `if`. Based on these conditions, the program decides if the user is eligible for a discount.

#### 4. Multiple `if` Statements (Independent Conditions)

**Scenario**: A smart home system that checks several independent conditions to set up the house for the night.

```python
lights_on : bool = True
doors_locked : bool = False
windows_closed : bool = True

if lights_on:
    print("Turning off the lights.")
if not doors_locked:
    print("Locking the doors.")
if windows_closed:
    print("All windows are closed.")
```

**Explanation**: Each `if` statement is independent and checks a different condition. The system performs actions like turning off lights, locking doors, and checking windows, regardless of the other conditions.


#### 5. Nested `if` with `elif` and `else`

**Scenario**: A restaurant ordering system that checks if a user has chosen a meal and then checks for special requests.

```python
meal_selected : str = "burger"
add_cheese : bool = True

if meal_selected == "burger":
    print("Burger selected.")

    if add_cheese:
        print("Adding cheese.")
    else:
        print("No cheese added.")

elif meal_selected == "pizza":
    print("Pizza selected.")
else:
    print("Please select a meal.")
```

**Explanation**: The system first checks if a meal is selected, then performs additional checks (like adding cheese) using nested `if` statements. If the meal isn’t a burger, it checks for other meals with `elif`.

These examples illustrate how `if`, `elif`, nested `if`, and multiple independent `if` statements can be used to handle various real-world scenarios in Python.

-------------------

## 6.  Logical Operators in Python

### The Problem: Making Complex Decisions in Code

Imagine we're developing a security system for a smart home. The system should lock the doors if it's nighttime and the user is away, or if it's daytime and the user has set the system to "vacation mode." But there's a catch: we need to ensure that the system doesn't lock the doors when the user is home, even if the other conditions are met. 

How do we make our code handle these multiple, interconnected conditions? Without a way to combine and evaluate these conditions simultaneously, our security system might fail to work properly, leaving the house unprotected when it should be locked, or worse, locking the user out of their own home.

This brings us to a critical concept in programming: **Logical Operators**.

### The Solution: Combining Conditions with Logical Operators

In Python, **Logical Operators** (`and`, `or`, `not`) are essential tools that allow we to combine multiple conditions in our code. They enable our program to make complex decisions by evaluating whether a group of conditions are true or false.

#### The Story of Complex Decisions: `and`, `or`, and `not`

Let's explore how Python uses logical operators to manage complex scenarios in our code.

1. **The `And` Operator**:
   - Imagine we need to check if two conditions are both true. The `and` operator allows we to combine these conditions so that the flow of our program continues only if both are met.
   - In our smart home example, we want to lock the doors only if it’s nighttime **and** the user is away.

    ```python
    is_night : bool = True
    is_user_away : bool = True
    
    if is_night and is_user_away:
        print("Lock the doors.")
    ```

2. **The "Or" Operator**:
   - Sometimes, we want to take action if at least one of several conditions is true. The `or` operator allows our program to proceed if any of the combined conditions are met.
   - For instance, we want to lock the doors if it’s either nighttime and the user is away **or** if the system is in "vacation mode."

    ```python
    is_vacation_mode : bool = True
    
    if (is_night and is_user_away) or is_vacation_mode:
        print("Lock the doors.")
    ```

3. **The "Not" Operator**:
   - There are situations where we need to reverse a condition. The `not` operator inverts the truth value of a condition, allowing our program to act when something is **not** true.
   - In our case, we don’t want to lock the doors if the user is home, regardless of the other conditions.

    ```python
    is_user_home : bool = False
    
    if (is_night and is_user_away) or is_vacation_mode and not is_user_home:
        print("Lock the doors.")
    else:
        print("Do not lock the doors.")
    ```

### Why It Matters

Logical operators are the backbone of complex decision-making in our code. They allow we to evaluate multiple conditions at once, enabling our program to handle intricate scenarios with ease. By combining conditions with `and`, `or`, and `not`, we can create powerful, flexible logic that adapts to a variety of situations.

With logical operators, we can solve problems like:

- **Implementing security checks**: Ensure that multiple criteria are met before taking critical actions.
- **Building advanced user interfaces**: Display different content based on a combination of user settings.
- **Creating sophisticated algorithms**: Make our code smarter by evaluating multiple factors simultaneously.

### Conclusion

Mastering logical operators is essential for writing code that can handle complex, real-world scenarios. Whether we're working on a security system, a game, or a web application, understanding how to combine conditions with `and`, `or`, and `not` will allow we to build more intelligent, responsive programs.



### Examples


#### Scenario: Finding a Life Partner

Imagine you're looking for a life partner, and you have certain qualities in mind that are important to you. Specifically, you want your partner to be either **handsome** and also **well-educated**. You can use logical operators to determine if a potential partner meets these criteria.

#### 1. Using the `and` Operator

You want to ensure that the person is both **handsome** and **well-educated**. Both conditions must be true for the person to be considered.

```python
is_handsome : bool = True
is_well_educated : bool = True

if is_handsome and is_well_educated:
    print("This person might be a great match!")
else:
    print("Keep looking for someone with both qualities.")
```

**Explanation**: The `and` operator ensures that only if the person is both good-looking (`is_handsome`) **and** well-educated (`is_well_educated`), the program will suggest that the person might be a great match.

#### 2. Using the `or` Operator

Now, let's say you’re a bit more flexible, and you’re open to considering someone who either has good looks or is well-educated (or both).

```python
is_handsome : bool = False
is_well_educated : bool= True

if is_handsome or is_well_educated:
    print("This person could be a good match!")
else:
    print("Keep looking for someone who meets at least one of your criteria.")
```

**Explanation**: The `or` operator allows for more flexibility. If the person meets at least one of the criteria—either being handsome **or** well-educated—the program suggests that this person could still be a good match.

#### 3. Using the `not` Operator

Let’s add another layer. Suppose you want to avoid someone who is not well-educated, regardless of whether they are handsome.

```python
is_handsome : bool = True
is_well_educated : bool = False

if is_handsome and not is_well_educated:
    print("This person is attractive but not well-educated.")
else:
    print("This person is either well-educated, or both attractive and well-educated.")
```

**Explanation**: Here, the `not` operator inverts the `is_well_educated` condition. If the person is attractive but not well-educated, the program points out the lack of education. Otherwise, it suggests that the person meets at least the education criterion or both.

#### 4. Combining Multiple Logical Operators

Finally, let's say you have a scenario where you want to find someone who is either well-educated **and** handsome, or at least has one of these qualities.

```python
is_handsome : bool = False
is_well_educated : bool = True
is_high_income : bool = True

if (is_handsome and is_well_educated) or is_high_income:
    print("This person is well-educated, which is important to you.")
else:
    print("Keep looking for someone who fits your criteria better.")
```

**Explanation**: This condition checks for either both qualities being present, or at least being well-educated. The logical operators `and`, `or`, and `not` allow you to evaluate complex conditions and make more nuanced decisions.
