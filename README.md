# Cython Timer Decorator

A small timing decorator implemented in Cython for measuring 
function execution time with minimal overhead, just for fun.

The module provides a single decorator `timer` that measures and returns 
the execution time of decorated functions alongside their results.

## Example:

```python
@timer
def expensive_operation(n):
  return sum(i * i for i in range(n))

result, exec_time = expensive_operation(1000000)
print(f"Result: {result}, Time: {exec_time:.6f} seconds")
```

## Features:
- Minimal measurement overhead using C standard library clock()
- Preserves function arguments and return values
- Returns both result and execution time as a tuple
- Compatible with functions of any signature (i think?)

> [!NOTE]  
> Uses processor clock ticks for timing, which provides high precision but may not account for time spent in sleep or I/O operations.

## Installation:
1. Clone this repository
2. `cd cytimer`
3. `pip install .`

---

### Version: 0.1.0
