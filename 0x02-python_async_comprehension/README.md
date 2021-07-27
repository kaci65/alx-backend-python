### 0x02-python_async_comprehension

### Resources
    [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
    [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
    [Type-hints for generators](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    How to write an asynchronous generator
    How to use async comprehensions
    How to type-annotate generators

### Tasks
### 0-async_generator.py
Write a coroutine called async_generator that takes no arguments
The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module

### 1-async_comprehension.py
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments
The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers

### 2-measure_runtime.py
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather
measure_runtime should measure the total runtime and return it

Notice that the total runtime is roughly 10 seconds, explain it to yourself

### Extra Resources
    [Python Asynchronous Comprehensions - how do they work?](https://stackoverflow.com/questions/42335754/python-asynchronous-comprehensions-how-do-they-work)
    [Python Typing: Optional](https://docs.python.org/3/library/typing.html#typing.Optional)
    [TypeError: 'task() takes 0 positional arguments but 1 was given' for python asyncio function](https://stackoverflow.com/questions/68405285/task-takes-0-positional-arguments-but-1-was-given-for-python-asyncio-functio)
    [Type hinting generator in python 3.6](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)
    [PEP 525 -- Asynchronous Generators](https://www.python.org/dev/peps/pep-0525/)
