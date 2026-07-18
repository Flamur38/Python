
### What are the two values of the Boolean data type? How do you write them?
`True`, `False`

### What are the three Boolean operators?
and, or, not

### Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |


### What do the following expressions evaluate to?
```python
(5 > 4) and (3 == 5)                    # False
not (5 > 4)                             # False
(5 > 4) or (3 == 5)                     # True
not ((5 > 4) or (3 == 5))               # False
(True and True) and (True == False)     # False
(not False) or (not True)               # True
```


### What are the six comparison operators?
==
!=
>
<
>=
<=

### What is the difference between the equal to operator and the assignment operator?
Assignment: name = "Flamur"
comparison: name == 'flamy'

### Explain what a condition is and where you would use one.
Example:
```python
if login_failed:
    alert()
else:
    allow_access()
```

### Identify the three blocks in this code:
```python
spam = 0
if spam == 10:          # 1
    print('eggs')
    if spam > 5:        # 2
       print('bacon')
    else:               
        print('ham')
    print('spam')
print('Done')           # 3
```


### Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```python
spam = 'something'

if spam == 1:
    print('Hello')

elif spam == 2:
    print('Howdy')

else:
    print('Greetings!')

```
