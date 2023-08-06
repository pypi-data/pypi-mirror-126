# Functional Recursion
Do tail recursion without overflowing with generators and functions.

## Why?
I am coming from a background of functional programming languages where loops are not standard. Instead, recursion is used to achieve the same result more succinctly.

## Overview
It provides:
* Infinite recursion with return
* Infinite recursion with generators (yield)

Using this has the following advantages:
* Allows for more understandable code given the right situation
* Avoid bugs because of deeply nested loops

## Instructions
Run in the console
```bash
python3 -m pip install functional_recursion
```
(Use `python` or `python3` depending on your environment)

And to use it

```python
from functional_recursion import recur, recur_yield, tail_recursive, tail_recursive_yield

@tail_recursive
def fib_decorator_recursive(n, last_two=None):
    if last_two is None:
        last_two = (0, 1)
    if n == 0:
        return last_two[1]
    last_two = (last_two[1], sum(last_two))
    return recur(n - 1, last_two)


@tail_recursive_yield
def fib_decorator_recursive_generator(last_two=None):
    if last_two is None:
        last_two = (0, 1)
    last_two = (last_two[1], sum(last_two))
    return recur_yield(last_two, yield_val=last_two[0])
```
\* See the complete examples and performance times [here](https://github.com/hunterwilhelm/functional-recursion/tree/master/examples).

## Authors
* [Hunter Wilhelm](https://github.com/hunterwilhelm)
