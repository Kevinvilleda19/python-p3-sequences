#!/usr/bin/env python3

def print_fibonacci(length):
    if length <=0:
        print([])
        return
    if length ==1:
        print([0])
        return
    if length == 2:
        print([0,1])
        return
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence iteratively for lengths greater than 2
    for i in range(2, length):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # Print the entire Fibonacci sequence up to the specified length
    print(fibonacci_sequence)