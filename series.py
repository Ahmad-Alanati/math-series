fibonacci_list = [0,1]
lucas_list = [2,1]
sum_series_list =[]

def fibonacci(n):
    if not isinstance(n,int) or n<0:
        respons = "there is no fibonacci number for this {} {}"
        return respons.format(type(n),n)
    if n in range(len(fibonacci_list)):
        return fibonacci_list[n]
    else:
        fibonacci_list.append(fibonacci(n-1)+fibonacci(n-2))
        return fibonacci_list[n]

def lucas(n):
    if not isinstance(n,int) or n<0:
        respons = "there is no lucas number for this {} {}"
        return respons.format(type(n),n)
    if n in range(len(lucas_list)):
        return lucas_list[n]
    else:
        lucas_list.append(lucas(n-1)+lucas(n-2))
        return lucas_list[n]

def sum_series(n,first_element=0,second_element=1):
    print(sum_series_list)
    if len(sum_series_list) == 0:
        sum_series_list.append(first_element)
        sum_series_list.append(second_element)
    if not isinstance(n,int) or not isinstance(first_element,int) or not isinstance(first_element,int):
        return "one of the pram isn't an int"
    if n in range(len(sum_series_list)):
        return sum_series_list[n]
    else:
        sum_series_list.append(sum_series(n-1)+sum_series(n-2))
        return sum_series_list[n]
    
def sum_series_list_delete():
    sum_series_list.clear()
