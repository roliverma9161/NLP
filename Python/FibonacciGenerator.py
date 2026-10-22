def generate_fibonacci(n_terms):
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n_terms):
        next_val = fib[-1] + fib[-2]
        fib.append(next_val)
    return fib

terms = 10
print(f"First {terms} terms of Fibonacci sequence: {generate_fibonacci(terms)}")