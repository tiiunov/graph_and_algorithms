import psutil


def mem_of_function(function):
    def wrapped(*args):
        start_mem = psutil.virtual_memory().used
        res = function(*args)
        print(f'50001 поиск пути  {psutil.virtual_memory().used - start_mem}')
        return res
    return wrapped
