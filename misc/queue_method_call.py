def run(self):
    """
    demo of using sched to queue method calls and get them executed manually
    ref. https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/sched/index.html
    ref. https://docs.python.org/2/library/sched.html
    """

    def f1(): return print(1)

    def f2(n): return print(n)

    def f3(): return print(333)

    def f4(n, m): return print(n, m)

    import sched
    s = sched.scheduler()
    s.enter(0, 0, f1)
    s.enter(0, 0, f2, (22,))
    f3()
    s.enter(0, 0, f4, (4, 55))
    s.run()

run()