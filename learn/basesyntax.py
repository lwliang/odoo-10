import time


def add(x, y):
    return x + y


params_list = (1, 2)


def foo(func):
    print "decorator foo"
    return func


@foo
def bar():
    print 'bar'


def function_performance_statistics(trace_this=True):
    if trace_this:
        def performance_statistics_delegate(func):
            def counter(*args, **kwargs):
                start = time.clock()
                func(*args, **kwargs)
                end = time.clock()
                print 'used time : %d' % (end - start,)

            return counter
    else:
        def performance_statistics_delegate(func):
            return func
    return performance_statistics_delegate


@function_performance_statistics(True)
def add(x, y):
    time.sleep(3)
    print 'add result: %d' % (x + y,)


@function_performance_statistics(False)
def mul(x, y=1):
    print 'mul result: %d' % (x * y,)


def bar(dummy):
    print 'bar'


def inject(cls):
    cls.bar = bar
    return cls


@inject
class Foo(object):
    pass


foo = Foo()
foo.bar()