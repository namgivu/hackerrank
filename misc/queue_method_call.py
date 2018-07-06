"""
demo of using sched to queue method calls and get them executed manually
ref. https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/sched/index.html
ref. https://docs.python.org/2/library/sched.html
"""


def run1():
    def f1(): print(1)

    def f2(n): print(n)

    def f3(): print(333)

    def f4(n, m): print(n, m)

    import sched
    s = sched.scheduler()
    s.enter(0, 0, f1)
    s.enter(0, 0, f2, (22,))
    f3()
    s.enter(0, 0, f4, (4, 55))
    s.run()


def run2():
    def f5(*args, **kwargs):
        print(args)
        print(kwargs)

    import sched
    s = sched.scheduler()
    f5(1,22, a=333, b=4444)
    s.enter(0, 0, action=f5, argument=(1,22), kwargs=dict(a=333, b=4444) )
    s.run()

run2()