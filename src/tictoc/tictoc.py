'''
In MATLAB, tic works with the toc function to measure the elapsed time.

tic
-----
Calling tic() on its own should work with toc() to measure elapsed time

Assigning a var to the output of tic() should store output into a variable to be used later

toc
---
Calling toc() can do a few things
1. Calling with no args uses the global timer for elapsed time
2. Calling multiple times will give elapsed time since first tic
3. Calling with timer from tic() gives elapsed time for that specific timer
4. Assigning to var will give elapsed time without printing output
'''

import inspect
import dis

from time import time
from typing import Optional

_global_timer = None

class Timer:

    def __init__(self):
        self.start_time = time()

    @property
    def elapsed_time(self):
        return time() - self.start_time

    def reset(self):
        self.start_time = time()




def _is_assigned_to_var(frame):
    """Checks to see if function was called on its own, or if it was assigned to a variable"""

    instruction = frame.f_code.co_code[frame.f_lasti + 2]  # +2 accounts for 2-byte long function signature

    opname = dis.opname[instruction]

    if opname.startswith('POP_'):
        return False

    return True


def tic():

    global _global_timer

    calling_frame = inspect.stack()[1].frame
    timer = Timer()

    if _is_assigned_to_var(calling_frame):
        return timer

    _global_timer = timer


def toc(timer: Optional[Timer] = None):
    """Prints the elapsed time. If assigned to a variable, returns the elapsed time (in seconds)"""

    if not _global_timer and not timer:
        raise RuntimeError('Global timer has not been initiated. Please run tic() before running toc().')

    calling_frame = inspect.stack()[1].frame
    is_assigned_to_var = _is_assigned_to_var(calling_frame)

    if not timer:
        if is_assigned_to_var:
            return _global_timer.elapsed_time
        print(f'Elapsed time is {_global_timer.elapsed_time} seconds.')
        return

    if is_assigned_to_var:
        return timer.elapsed_time

    print(f'Elapsed time is {timer.elapsed_time} seconds.')
    return

def func_timer(func):
    def timer_wrapper(*args, **kwargs):
        _func_timer = tic()
        func(*args, **kwargs)
        print(f'Elapsed time for function {func.__name__} is {toc(_func_timer)} seconds.')
    return timer_wrapper
