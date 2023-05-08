fibonacci_list = [0,1]


def fibonacci(n):
    if n in range(len(fibonacci_list)):
        return fibonacci_list[n]
    else:
        fibonacci_list.append(fibonacci(n-1)+fibonacci(n-2))
        return fibonacci_list[n]

def lucas(n):
    return 2

def sum_series(n,first_element=0,second_element=1):
    return n