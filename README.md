# Programming Assignment 2

## Course: CSCI 360 - Introduction to Artificial Intelligence

-----

## Setting up the environment

You can either use the environment created for lab 1 or use the following commands to create a new one.

```
git clone YOUR-GITHUB-REPO-HERE && cd CSCI360-lab2
conda env create --name cs360_lab2
conda activate cs360_lab2
pip install -r requirements.txt
```

## Writing your code

- All of the code that will be evaluated and graded will live in
[`lab2.py`](lab2.py).
- You can use any python package that is installed by `pip` or `conda`
when you created the environment.
- You are provided with [`lab2_utils.py`](lab2_utils.py) which contains
the `TextbookStack` class. Same as lab 1, the constructor for this class expects two
lists that represent the order. The first list `initial_order` is a
list of length `n` that expects each integer `[0, n-1]` to be present
once. The second list `initial_orientation` should be a list of length
`n` of exclusively `0`s and `1`s, which represent the whether Textbook faces up.

## Testing your code

We have given you example tests that you can run from the terminal by
invoking:

```
python test.py
```

from inside your the directory. These are starting points that reflect
the same type of tests that we will run in order to evaluate and grade
the correctness of your algorithm.

## How we will grade
### Main part (max 100 pts; problem 2)
- General soundness of your code (60 pts): You should provide full implementation of function `a_star_search` with comprehensible comments. If your code does not implement the required algorithm, we will deduct points from the 60 pts.
- Passing multiple test cases (40 pts): 
	- Part 1 (24 pts): Your program should pass three example test cases with correct sequences. Each test case worths 8 pts. If your implementation is correct, testing should generate output as follows:
	```
	>>> python test.py 
	Generating A* solutions
	[4]
	[2, 1, 2, 4, 2]
	[4, 6, 5, 1, 4, 1, 2]
	Tests:3 - Passed: 3 - Confirmed Sequ: 3
	```
	- Part 2 (16 pts): We will further test your implementation through all permutations of stacks. As commented in `test.py`, you should change `max_n` to an arbitrary number and see if your program runs correctly and efficiently. Increasing this number can increase time lapse dramatically. We will test `max_n` for at least 4. For example, `max_n=4` costs up to 4 seconds; `max_n=5` costs around 2 minutes; `max_n=6` costs as long as 150 minutes. If your implementation is correct, testing should generate output as follows:
	```
	Evaluating A* on all permutations
	Passing 100.0 %
	Time lapse for max_n=4: 1.618 seconds.
	```

### Extra credit (max 20 pts; problem 3)
- Similar to lab1, you will upload an extra PDF file named "lab2_extra_credit.pdf" in this repository. If we cannot find a file named this, you will receive 0 pts for extra credit part.
- Besides the two tables required as in instruction, you must provide implementation in function `weighted_a_star_search` with comprehensible comments. Otherwise, you will receive at most 10 points.

## Documentation (same as lab 1)
```
>>> from lab2_utils import TextbookStack

# Construct a stack of books in reverse order
>>> stack = TextbookStack(initial_order=[2, 1, 0], initial_orientations=[0, 0, 0])
>>> print(stack)
TextbookStack:
 	 order: [2 1 0]
	 orientations:[0 0 0]
```

- You can access the current order and orientation of the books by
accessing the attributes `TextbookStack.order` and
`TextbookStack.orientations` respectively.

```
>>> stack.order
array([2, 1, 0])
>>> stack.orientations
array([0, 0, 0])
```

- Calling the command `flip_stack(position)` will flip the books up to the
`position`. For example if you want to flip the top book of your `stack`
you should call `stack.flip_stack(1)`.

```
>>> stack.flip_stack(2)
>>> stack.order
array([1, 2, 0])
>>> stack.orientations
array([1, 1, 0])
```

- You can make a copy of a stack by invoking the `.copy()` this will
create a new object with the same current order and orientations as the
stack from which you invoked the method. You can use `==` to compare the
equivalence of two stacks.

```
>>> new_stack = stack.copy()
>>> new_stack == stack
True
>>> new_stack.flip_stack(3)
>>> new_stack == stack
False
```


- Finally, you can check if the stack is ordered by invoking the
`check_ordered`

```
>>> stack.check_ordered()
False
>>> stack.flip_stack(2)
>>> stack.flip_stack(3)
>>> stack.check_ordered()
True
```
- All of your algorithm should be contained in the designated blocks
inside of `a_star_search` and `weighted_a_star_search` and should
return the sequence of flips that your search algorithms find.


