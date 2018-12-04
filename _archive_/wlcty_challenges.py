'''
Ch01
Given two numbers that are represented as arrays of their digits, write a function that returns the sum of the two numbers.
Each number is represented by an array of integers from 0 to 9, with the first element being the most significant digit of a number and the last element being the least significant digit.
Note: Try to solve this task using only addition between digits.

Example

- For a = [1, 0] and b = [5], the output should be integerAdder(a, b) = [1, 5];
- For a = [2, 6] and b = [3, 4], the output should be integerAdder(a, b) = [6, 0].

Consider the following conditions:

Input:

- array.integer a
  Guaranteed constraints: 1 ≤ a.length ≤ 50, 0 ≤ a[i] ≤ 9.
- array.integer b
  Guaranteed constraints: 1 ≤ b.length ≤ 50, 0 ≤ b[i] ≤ 9.

Output:

- array.integer
  - The result of adding a and b together
  - Each position can contain only digits (0-9)

'''




'''
Ch02
Write a function to check for brackets in a string expression. The brackets in the expression should be balanced, but also coherent.

Consider only ( ), [ ], { } as valid bracket indicators

Examples

input: '[()]{}{[()()]()}'
output: true

intput: '[(])'
output: false
'''
