import timeit


def time_of_function(function):
    def wrapped(*args):
        start_time = timeit.default_timer()
        res = function(*args)
        print(f'50001 поиск пути - {timeit.default_timer() - start_time} сек.')
        return res
    return wrapped
