def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

##First solution
##def car(pair):
##    return pair.__closure__[0].cell_contents
##
##
##def cdr(pair):
##    return pair.__closure__[1].cell_contents
##
##print(car(cons(5,4)))
##print(cdr(cons(5,4)))


##Second solution
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





##result=cons(5,4)
##print(result)
##result(print)
##cons(5,4)(print)
##print(result.__closure__)
##print(result.__closure__[0].cell_contents)
##print(result.__closure__[1].cell_contents)
