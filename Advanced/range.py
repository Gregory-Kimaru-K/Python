def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    results = []

    if step < 0:
        while start > stop:
            results.append(start)
            start += step

    elif step > 0:
        while start < stop:
            results.append(start)
            start += step

    return results

print(custom_range(10))
print(custom_range(1, 11))
print(custom_range(1, 201, 10))