# Assignments for Class 04

## Assignment-01

Use chatgpt/gemini to learn the below concept

- A string 'Rehan' is stored in a variable `name`.
- A list named 'teacher_names' is created and added 'Rehan' as one value in the list.
- Find out that the if the same memory address is used for both the variable and the list.

**\*hint:** use `id()` function to find the memory address of the variable and the list.\*

## Assignment-02

Find out all the methods of the sting in python using `dir()` function.
Leave methods starting with `__`.
Use each string method in code and write the discription of it.

**\*hint:** use below code to find out all available string methods\*

```python
sting_methods = [method for method in dir(str) if not method.startswith('__')]
print(sting_methods)
```

## Assignment-03

Find out all the methods of the list in python using `dir()` function.
Use each list method in code and write the discription of it.

**\*hint:** use below code to find out all available list methods\*

```python
list_methods = [method for method in dir(list) if not method.startswith('__')]
print(list_methods)
```

## Assignment-04

Read about variable naming rules and conventions in python.
