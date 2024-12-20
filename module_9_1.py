def apply_all_func(int_list, *functions):
    results = {}
    try:
        for function in functions:
            results[function.__name__] = function(int_list)
    except TypeError:
        print('Некорректный тип данных в списке')
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, '20', 15, 9], max, min))
