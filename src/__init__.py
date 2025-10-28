"""
Cython Timer Decorator

A small timing decorator implemented in Cython for measuring 
function execution time with minimal overhead, just for fun.

The module provides a single decorator `timer` that measures and returns 
the execution time of decorated functions alongside their results.

Example:

    from cytimer import timer
    
    @timer
    def expensive_operation(n):
        return sum(i * i for i in range(n))
    
    result, exec_time = expensive_operation(1000000)
    print(f"Result: {result}, Time: {exec_time:.6f} seconds")

Features:
    - Minimal measurement overhead using C standard library clock()
    - Preserves function arguments and return values
    - Returns both result and execution time as a tuple
    - Compatible with functions of any signature

Note:
    Uses processor clock ticks for timing, which provides high precision
    but may not account for time spent in sleep or I/O operations.

Version: 0.1.0
"""

from . import timer

__all__ = ["timer"]
__version__ = "0.1.0"