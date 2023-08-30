cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = fibonacci(n - 1)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))