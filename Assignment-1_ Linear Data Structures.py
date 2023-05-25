#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs(array, target_sum):
    pairs = []
    seen = set()

    for num in array:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs


array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
result = find_pairs(array, target_sum)
print(result)


# In[13]:


#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


array = [1, 2, 3, 4, 5]
reverse_array(array)
print(array)


# In[3]:


#Q3. Write a program to check if two strings are a rotation of each other?

def are_rotations(string1, string2):
    if len(string1) != len(string2):
        return False

    concatenated = string1 + string1
    if string2 in concatenated:
        return True
    else:
        return False


string1 = "abcd"
string2 = "cdab"
result = are_rotations(string1, string2)
print(result)


# In[4]:


#Q4. Write a program to print the first non-repeated character from a string?

def find_first_non_repeated_character(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None


string = "abracadabra"
result = find_first_non_repeated_character(string)
print(result)


# In[5]:


#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, auxiliary, destination):
    if n > 0:
        tower_of_hanoi(n-1, source, destination, auxiliary)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1, auxiliary, source, destination)


n = 3
tower_of_hanoi(n, 'A', 'B', 'C')


# In[6]:


#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def is_operator(char):
    operators = ['+', '-', '*', '/']
    return char in operators

def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)
        else:
            stack.append(char)

    return stack.pop()


postfix_expression = "ab+cde+**"
prefix_expression = postfix_to_prefix(postfix_expression)
print(prefix_expression)


# In[7]:


#Q7. Write a program to convert prefix expression to infix expression.

def is_operator(char):
    operators = ['+', '-', '*', '/']
    return char in operators

def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f"({operand1}{char}{operand2})"
            stack.append(infix)
        else:
            stack.append(char)

    return stack.pop()


prefix_expression = "**+abc+de"
infix_expression = prefix_to_infix(prefix_expression)
print(infix_expression)


# In[8]:


#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []

    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]
    brackets_map = {")": "(", "}": "{", "]": "["}

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[char] != stack.pop():
                return False

    return len(stack) == 0


code_snippet = "{(a + b) * [c - d]}"
result = check_brackets(code_snippet)
print(result)


# In[9]:


#Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_stack(stack):
    if stack.is_empty():
        return

    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        top_item = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(top_item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
reverse_stack(stack)

while not stack.is_empty():
    print(stack.pop())


# In[14]:


#Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []
        self.minimum = float('inf')

    def push(self, item):
        if item < self.minimum:
            self.minimum = item
        self.items.append((item, self.minimum))

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()[0]

    def is_empty(self):
        return len(self.items) == 0

    def get_minimum(self):
        if self.is_empty():
            return None
        return self.items[-1][1]


stack = Stack()
stack.push(4)
stack.push(2)
stack.push(5)
stack.push(1)

print(stack.get_minimum())  # Output: 1

stack.pop()
stack.pop()

print(stack.get_minimum())  # Output: 2


# In[ ]:




