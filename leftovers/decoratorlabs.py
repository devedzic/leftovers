# Create a decorator that measures the time a function takes to execute and prints the duration to the console.
# Create also a couple of simple functions to test the decorator and decorate them accordingly.
# Hint 1: use the decorator-writing pattern:
# import functools
# def decorator(func):
#     @functools.wraps(func)			                # preserves func's identity after it's decorated
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator
# Hint 2: to measure the time a function takes, use the time.perf_counter() function from the Python Standard Library.


def stopwatch(f):                                       # alt. names: runtime, running_time, timer, get_time, interval

    import functools                                    # can be imported somewhere on top of the module as well

    @functools.wraps(f)
    def stopwatch_wrapper(*args, **kwargs):
        import time                                     # can be imported somewhere on top of the module as well

        # Do something before
        print('Running', f.__name__ + '(' + ','.join([str(arg) for arg in args]) + ')...')
        start_time = time.perf_counter()

        v = f(*args, **kwargs)

        # Do something after
        end_time = time.perf_counter()
        print('Time:', '{0:.5f}'.format(end_time - start_time), 'sec.')

        return v

    return stopwatch_wrapper


@stopwatch
def sum_of_squares(n, **kwargs):                        # test function 1
    for _ in range(n):
        sum([i * i for i in range(10000)])

@stopwatch
def sum_of_powers(x, y, n):                             # test function 2
    if x not in range(1, 4):                            # constrain input parameters for the sake of running time
        x = 3
    if y not in range(1, 4):
        y = 3
    if n not in range(1, 1000):
        n = 999
    for _ in range(n):
        sum([i**x + i**y for i in range(10000)])


# Create a decorator that makes a function run with a delay of n sec (n should be the decorator parameter).
# Create also a couple of simple functions to test the decorator and decorate them accordingly.
# Hint 1: use the "extended" decorator-writing pattern:
# def decorator(arg1, arg2, ...):
#     def real_decorator(func):
#         import functools
#         @functools.wraps(func)			            # preserves func's identity after it's decorated
#         def wrapper_real_decorator(*args, **kwargs):
#             # Do something before
#             some_stuff()
#             some_stuff_with_arguments(arg1, arg2, ...)
#             value = func(*args, **kwargs)
#             # Do something after
#             more_stuff()
#             return value
#         return wrapper_real_decorator
#     return real_decorator
# Hint 2: use the time.sleep() function from the Python Standard Library to introduce the delay.

def delay(n):

    def wait(f):

        import functools                                # can be imported somewhere on top of the module as well

        @functools.wraps(f)
        def wrapper_wait(*args, **kwargs):
            import time                                 # can be imported somewhere on top of the module as well

            # Do something before
            time.sleep(n)                               # improves output visually
            print('Wait', n, 'sec...')
            time.sleep(n)

            v = f(*args, **kwargs)

            # Do something after

            return v

        return wrapper_wait

    return wait


@delay(1)
# @wait
def print_list_elements(l):
    while l:                                            # l != []
        print(l[0])
        del(l[0])
        print_list_elements(l)


if __name__ == '__main__':

    # sum_of_squares(100)
    # sum_of_powers(2, 3, 200)

    l = ["Bruce Springsteen", "Patti Smith", "Alejandro Escovedo"]
    print_list_elements(l)

