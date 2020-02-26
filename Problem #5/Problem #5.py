def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


##result=cons(5,4)
##print(result)
##result(print)
##cons(5,4)(print)
##print(result.__closure__)
##print(result.__closure__[0].cell_contents)
##print(result.__closure__[1].cell_contents)


##def car(pair):
##    return pair.__closure__[0].cell_contents
##
##
##def cdr(pair):
##    return pair.__closure__[1].cell_contents
##
##print(car(cons(5,4)))
##print(cdr(cons(5,4)))

def car(pair):
    def return_first(a, b):
        return a
    return pair(return_first)


def cdr(pair):
    def return_last(a, b):
        return b
    return pair(return_last)


print(car(cons(5,4)))
print(cdr(cons(5,4)))


###################
##cons(42,81)
##pair(f):
##    return f(42,81)
##pair
##car(pair)
##return pair(return_first)
##pair(return_first):
##    return return_first(42,81)
