### 0x01-python_async_function

### Resources
    Async IO in Python: A Complete Walkthrough: <https://realpython.com/async-io-python/>
    asyncio - Asynchronous I/O: <https://docs.python.org/3/library/asyncio.html>
    random.uniform: <https://docs.python.org/3/library/random.html#random.uniform>

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
    async and await syntax
    How to execute an async program with asyncio
    How to run concurrent coroutines
    How to create asyncio tasks
    How to use the random module

### Tasks
#### 0-basic_async_syntax.py
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module

#### 1-concurrent_coroutines.py
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency

#### 2-measure_runtime.py
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time

#### 3-tasks.py
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task

#### 4-tasks.py
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called


#### NB:
Run .main files with python3.7 instead of just python3, example:
	>>> python3.7 filename <correct>
	>>> python3 filename <avoid>

Why? -> https://stackoverflow.com/questions/52796630/python3-6-attributeerror-module-asyncio-has-no-attribute-run

#### Extra Resources:
    1. <https://stackoverflow.com/questions/46004745/python-async-co-routine-execution-time>
    2. <https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait>
    3. <https://stackoverflow.com/questions/62450624/asyncio-gather-with-generator-expression>
    4. <https://stackoverflow.com/questions/49005651/how-does-asyncio-actually-work>
    5. <https://medium.com/hackernoon/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c>
    6. <https://realpython.com/lessons/what-asyncio/>
    7. <https://medium.com/analytics-vidhya/python-generators-coroutines-async-io-with-examples-28771b586578>
