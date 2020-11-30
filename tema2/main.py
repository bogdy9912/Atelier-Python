# Ex 1:

def my_function(*args, **kargs):
    sum = 0
    for i in args:
        if (type(i) == type(1)) or (type(i) == type(3.2)):
            sum += i

    return sum


p = my_function(2, 4, 5, 6, -6, -5, -4, 3.2)
print(p)


# Ex 2:

def recursiv(n):
    if n == 1:
        return 1
    return n + recursiv(n-1)


def recursiv_pare(n):
    if n == 0:
        return 0
    if n%2 == 0:
        return n + recursiv_pare(n-2)
    else:
        return recursiv_pare(n-1)
def recursiv_impare(n):
    if n == 1:
        return 1
    if n%2:
        return n + recursiv_impare(n-2)
    else:
        return recursiv_impare(n-1)

# Ex 3:

def function():
    n = input('Introdu un numar:' )
    try:
        n = int(n)
        return n
    except:
        return 0

x = function()
print(x)
