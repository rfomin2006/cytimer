from libc.time cimport clock, clock_t, CLOCKS_PER_SEC

def timer(func):
    def wrapper(*args, **kwargs):
        return ctimer(func, args, kwargs)
    return wrapper

cdef ctimer(object func, tuple args, dict kwargs):
    cdef clock_t start, end
    start = clock()
    result = func(*args, **kwargs)
    end = clock()
    return result, (end - start) / CLOCKS_PER_SEC