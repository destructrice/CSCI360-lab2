from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque

def heuristic(stack):
    """
    Calculate the heuristic value h for the given stack of textbooks.
    """
    h = 0
    n = len(stack.stack) 
    
    for i in range(n):
        for j in range(i + 1, n):
            book_i = stack.stack[i]
            book_j = stack.stack[j]
            
            if abs(book_i - book_j) > 1:
                h += 1
            else:
                if (stack.stack[i] % 2 != stack.stack[j] % 2) or (book_i > book_j):
                    h += 1
            
    return h

def a_star_search(stack):
    flip_sequence = []

    fringe = [(0 + heuristic(stack), 0, stack, [])]

    while fringe:
        _, cost, current_stack, current_sequence = heappop(fringe)

        if current_stack.is_sorted():
            return current_sequence

        for i in range(len(current_stack)):
            for j in range(i + 1, len(current_stack)):
                new_stack = current_stack.copy()
                new_stack.flip(i, j)
                new_sequence = current_sequence + [(i, j)]
                new_cost = cost + 1

                heappush(fringe, (new_cost + heuristic(new_stack), new_cost, new_stack, new_sequence))

    return flip_sequence