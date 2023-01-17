

#pylint --disable all --enable spelling --spelling-dict en_US pylint_errors.py
# I am the tyop

def my_function():
    """ An example for a Pylint demonstration."""
    my_sum1 = 3 + 4
    print ("The sum is %d." % my_sum1)
    return my_sum


def my_function_unreachable():
    """ An example for a Pylint demonstration."""
    my_sum1 = 3 + 4
    print ("The sum is %d." % my_sum1)
    raise Exception("This shouldn’t happen.")
    return True


var = 1

def foo():
    global v
    print(v)
    v = 10
    print(v)

foo()
print(var)
