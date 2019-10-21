def demo_list():
    a = [1, 22, 333, 4444]
    print(f'a={a}')

    for i in range(0, len(a)):
        print(i)

    import sys;
    sys.exit()

    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
    print(f'even={even}')

    even = [i for i in a]
    print(f'even={even}')

    even = [i for i in a if i % 2 == 0]
    print(f'even={even}')

    odd = [i for i in a if i % 2 == 1]
    print(f'even={odd}')

def demo_dict():
    d = {
        'a' : 1,
        'bb': 22,
    }

    print(f'd={d}')

    d = dict(
        a  = 1,
        bb = 22,
    )
    print(f'd={d}')

    for k,v in d.items():
        print(f'k={k}: v={v}')
    print()

    for k in d.keys(): print(k)
    print()

    for v in d.values(): print(v)
    print()

    d1 = { 'a' : 1}
    d2 = { 'bb': 22}
    d3 = {**d1, **d2}
    print(f'd3={d3}')

def demo_infinite_params():

    def cong(*args):
        s = 0
        for i in args: s+=i
        return s

    c=cong();     print(f'c={c}')
    c=cong(1);    print(f'c={c}')
    c=cong(1,22); print(f'c={c}')

    c=cong(1,22,333);       print(f'c={c}')
    c=cong(1,22,333, 4444); print(f'c={c}')

    def max(a, b):
        return a if a>b else b

    def minn(a, b, c):
        return min(a, b, c)

    m=max(1,22);       print(f'm={m}')
    m=max(a=1,  b=22); print(f'm={m}')
    m=max(b=22, a=1);  print(f'm={m}')
    m=max(1, b=22);    print(f'm={m}')

    mi=minn(1,b=22,c=333); print(f'mi={mi}')

    def f(*args, **kwargs):
        print(f'args={args}')
        print(f'kwargs={kwargs}')

    print()
    f(1,22)
    f(1,b=22)

    def ff(a,bb,ccc,dddd,eeeee): pass
    ff(
        a=1,
        bb=1,
        ccc=1,
        dddd=1,
        eeeee=1,
    )

def demo_dict_comprehension():
    a = [1, 22, 333]

    d = { i:a[i] for i in range(0,len(a)) }
    print(f'd={d}')

    for i, v in enumerate(a):
        print(f'i={i} v={v}')

    d2 = { i:v for i,v in enumerate(a) }
    print(f'd2={d2}')

demo_dict_comprehension()
