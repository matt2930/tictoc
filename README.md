# Tic Toc

A Python module to make timing in python easier by mimicing MATLAB's `tic` and `toc` functions.
`tic` starts a timer by recording the current time, and `toc` uses the start time to find the elapsed time.

The included `func_timer` decorator uses `tic` and `toc` to give the elapsed time of the wrapped function.


## Usage

```
from tictoc import tic, toc

tic()              # starts the global timer
timer = tic()      # assigns an instance of the Timer class to the timer var without affecting the global timer

toc()              # Prints elapsed time from tic() call
toc(timer)         # Prints elapsed time for the timer given

time = toc(timer)  # Assigns elapsed time to a variable

timer.reset()      # Resets the timer var start time

tic()              # Restarts the global timer
```


## Examples

```
from time import sleep
from tictoc import tic, toc, func_timer


tic()  # starts global timer
sleep(1)
toc()
sleep(2)
toc()
```
>Elapsed time is 1.00547 seconds.

>Elapsed time is 3.00886 seconds.

```
timer = tic()
sleep(1)
print(f'Timer Assigned to var: {toc(timer)}')
print(f'Global Timer: {toc()}')
```
>Timer Assigned to var: 1.0057699

>Global Timer: 4.013537

```
@func_timer
def func():
    sleep(2)

func()
```
>Elapsed time for function func is 2.00556969 seconds.
