# README — Support Set (Crisp Set) Computation Using User Input in Python

# Introduction

This program demonstrates how to compute the **Support Set (Crisp Set)** of a fuzzy set using Python.

The program takes membership values from the user, stores them in a list, and then filters all values greater than `0`.

Those accepted values form the **Support Set**.

---

# What is a Fuzzy Set?

A fuzzy set is a set where elements can partially belong to the set.

Instead of only:

* `0` → False
* `1` → True

fuzzy logic allows values between `0` and `1`.

Example:

```python
[0.1, 0, 0.5, 0.7, 1]
```

Here:

| Value | Meaning            |
| ----- | ------------------ |
| `0`   | Not included       |
| `0.1` | Slightly included  |
| `0.5` | Partially included |
| `1`   | Fully included     |

---

# What is a Support Set?

The support set contains all values greater than `0`.

Mathematically:

```text
Support(A) = {x | μ(x) > 0}
```

Meaning:

* Include only values whose membership is greater than `0`

---

# Complete Program

```python
# Function to compute Support Set

def support(arr: list):

    print("These elements are present in support set:")

    for i in arr:

        if i > 0:
            print(i)


A1: list = []

n: int = int(input("Enter number of elements: "))

for i in range(n):

    value: float = float(input("Enter value: "))
    A1.append(value)


support(A1)
```

---

# Program Structure

The program is divided into three main parts:

| Section             | Purpose                      |
| ------------------- | ---------------------------- |
| Function Definition | Contains support set logic   |
| User Input Section  | Takes fuzzy values from user |
| Function Call       | Executes the program logic   |

---

# Step-by-Step Explanation

# 1. Function Definition

```python
def support(arr: list):
```

This creates a function named `support`.

## Why use a function?

Functions help:

* reuse code
* organize logic
* improve readability
* separate processing from input

---

# Parameter Explanation

```python
arr
```

`arr` is the parameter that receives the list.

When:

```python
support(A1)
```

is executed, Python internally does:

```python
arr = A1
```

---

# Type Hint

```python
: list
```

This tells the developer that the function expects a list.

---

# 2. Printing the Heading

```python
print("These elements are present in support set:")
```

This line prints the heading before showing the support elements.

---

# 3. Loop Traversal

```python
for i in arr:
```

This loop traverses every element inside the list.

Example:

```python
[0.1, 0, 0.5]
```

During iteration:

| Iteration | i   |
| --------- | --- |
| 1         | 0.1 |
| 2         | 0   |
| 3         | 0.5 |

---

# 4. Conditional Filtering

```python
if i > 0:
```

This is the core logic of the program.

The condition checks whether the membership value is greater than `0`.

---

# Why This Creates the Crisp Set

Before filtering:

```python
[0.1, 0, 0.5, 0.7, 1]
```

After filtering:

```python
0.1
0.5
0.7
1
```

This accepted collection becomes the support set.

The condition converts fuzzy membership logic into crisp inclusion logic.

---

# 5. Printing Accepted Values

```python
print(i)
```

If the condition becomes true, the value is printed.

Only values greater than `0` are displayed.

---

# 6. Creating the List

```python
A1: list = []
```

This creates an empty list.

The list stores all user-entered fuzzy membership values.

---

# 7. Taking Number of Elements

```python
n: int = int(input("Enter number of elements: "))
```

This line:

1. Takes input from the user
2. Converts it into integer type
3. Stores it in `n`

Example:

```python
5
```

means the user wants to enter 5 values.

---

# 8. Input Loop

```python
for i in range(n):
```

This loop runs `n` times.

If:

```python
n = 5
```

then the loop executes 5 times.

---

# 9. Taking Membership Values

```python
value: float = float(input("Enter value: "))
```

This line:

1. Takes user input
2. Converts it into decimal number
3. Stores it in `value`

---

# Why Float is Used

Fuzzy sets use decimal membership values.

Example:

```python
0.1
0.5
0.7
```

`int()` would not accept decimal numbers properly.

So `float()` is required.

---

# 10. Adding Values to the List

```python
A1.append(value)
```

This adds the entered value into the list.

Example:

```python
A1 = [0.1, 0, 0.5]
```

---

# 11. Function Call

```python
support(A1)
```

This sends the list into the function.

The function then starts processing the values.

---

# Complete Workflow

```text
User Enters Number of Elements
                |
Program Creates Empty List
                |
User Enters Fuzzy Membership Values
                |
Values Are Stored Inside List
                |
Function support(A1) Is Called
                |
Loop Traverses Each Value
                |
Condition Checks: i > 0
                |
Accepted Values Are Printed
                |
Support Set Is Generated
```

---

# Example Execution

## Input

```python
Enter number of elements: 5

Enter value: 0.1
Enter value: 0
Enter value: 0.5
Enter value: 0.7
Enter value: 1
```

---

# Output

```python
These elements are present in support set:
0.1
0.5
0.7
1.0
```

---



# | Concept   | Purpose                      |
  |           |                              |
  | Function  | Organizes logic               |
  | List      | Stores fuzzy values           |
  | Loop      | Traverses data                |
  | Condition | Filters valid elements        |
  | Float     | Handles decimal values        |
  | Type Hint | Improves readability          |
  | Iteration | Processes elements one-by-one |

---

# Principle Behind the Program

The program works on the principle of:

# Conditional Filtering

Every value is checked using:

```python
if i > 0
```

If true:

* the value belongs to the support set

If false:

* the value is ignored

This converts fuzzy membership data into crisp inclusion logic.

---

# Time Complexity

The loop traverses the list once.

Overall complexity:

```text
O(n)
```

where `n` is the number of elements.

---

# Final Conclusion

This program is a beginner-friendly implementation of support set computation in fuzzy logic.

It demonstrates:

* user input handling
* fuzzy membership representation
* list traversal
* filtering using conditions
* function-based program design

The implementation is clean, readable, and follows proper Python programming structure.
