# Scope - what variables do I have access to?
# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions

total = 0


def count_sum():
    # total+=1 - cannot do this because total is not declared in this def and hence error:
    # UnboundLocalError: local variable 'total' referenced before assignment
    global total  # not a good way to do it because it is quite confusing for us and other developers
    total += 1
    print(total)


def count_sum1(total):
    total += 1
    print(total)


# count_sum()
# count_sum1(10)


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
