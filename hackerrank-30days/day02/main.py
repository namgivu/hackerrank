import sys; sys.stdin = open('input')  # redirect input stream aka :stdin to file

# day 02
s=input(); meal = float(s)
s=input(); tip  = float(s)
s=input(); tax  = float(s)

cost = meal * (1 + tip/100.0 + tax/100.0)
print(f'cost={cost}')
