a = ['GUVI']
b=5
def foo(a,b):
    print a*b
def my_map_simple(fun, b):
    fun(a,b)

my_map_simple(foo, b)
