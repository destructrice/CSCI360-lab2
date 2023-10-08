from heapq import heappush, heappop
from lab2_utils import TextbookStack, apply_sequence
from collections import deque

def heuristic(stack):
    """
    Calculate the heuristic value h for the given stack of textbooks.
    """
    h = 0
    n = len(stack.order) 

    for i in range(n):
        for j in range(i + 1, n):
            book_i = stack.order[i]
            book_j = stack.order[j]
            orient_i = stack.orientations[i]
            orient_j = stack.orientations[j]

            # Condition: If the pair of books are not adjacent in the ordered stack, regardless of being face
            # up or face down.
            if abs(book_i - book_j) > 1:
                h += 1
            # Condition: If the pair has a book facing up and one facing down.
            if orient_i != orient_j:
                h += 1
            # Condition: If the pair is wrongly ordered, but with correct orientations (both facing up)
            elif book_i > book_j and orient_i == 1 and orient_j == 1:
                h += 1
            # Condition: If the pair is wrongly ordered, but with correct orientations (both facing up)
            elif book_i < book_j and orient_i == 0 and orient_j == 0:
                h += 1

    return h

def a_star_search(stack):
    flip_sequence = []

    # Python will throw an error when TextbookStack instances are compared. We need to put the stack at the end of tuple
    # elements in the heap should be: (total_cost, flip_cost, sequence, stack)
    fringe = [(0 + heuristic(stack), 0, [], stack)]

    # We should store hashes of visited states to improve speed
    visited = set()
    visited.add(hash(str(stack)))

    while fringe:
        total_cost, flip_cost, current_sequence, current_stack = heappop(fringe)

        if current_stack.check_ordered():
            return current_sequence

        for i in range(2, len(current_stack.order) + 1):
            new_stack = current_stack.copy()
            new_stack.flip_stack(i)  # flip i books from the top
            new_sequence = current_sequence + [i]
            new_cost = flip_cost + 1

             # Check if the current state has been visited before, if so, skip else add
            state_hash = hash(str(new_stack))
            if state_hash in visited:
                continue
            
            # Add the new state to visited states
            visited.add(state_hash)

            # Avoid TextbookStack instances comparison of Textbook Stack.
            # To do so, the TextbookStack instance should be placed at the end of the tuple.
            heappush(fringe, (new_cost + heuristic(new_stack), new_cost, new_sequence, new_stack))

    return flip_sequence