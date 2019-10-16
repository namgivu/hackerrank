import sys; sys.stdin = open('input')  # redirect input stream aka :stdin to file

n = input()
n = int(n)

if n % 2 == 1: print('Weird')
elif n % 2 == 0  and 2 <= n <= 5: print('Not Weird')
elif n % 2 == 0  and 6 <= n <= 20: print('Weird')
elif n % 2 == 0  and 20 < n: print('Not Weird')
