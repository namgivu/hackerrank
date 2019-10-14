import sys

# redirect input stream aka :stdin to file
old_stdin = sys.stdin
sys.stdin = open('input')

# day 01 code
i = 4
d = 4.0
s = 'HackerRank '

s1 = input()
s2 = input()
s3 = input()

t1=i + int(s1);   print(t1)
t2=d + float(s2); print(t2)
t3=s + s3;        print(t3)

