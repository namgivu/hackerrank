import sys

# redirect input stream aka :stdin to file
old_stdin = sys.stdin
sys.stdin = open('input')

# day 02
s=input(); meal = float(s)
s=input(); tip  = float(s)
s=input(); tax  = float(s)

cost = meal * (1 + tip/100.0 + tax/100.0)
print(f'cost={cost}')
