import sys

# redirect input stream aka :stdin to file
old_stdin = sys.stdin
sys.stdin = open('input')

# day 00 code
input_string = input()
print('Hello, World.')
print(input_string)

# restore stdin
sys.stdin = old_stdin
