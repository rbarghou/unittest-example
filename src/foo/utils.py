

def standard_deviation(values):
    n = float(len(values))
    mean = sum(values) / n
    sum_squared_variances = sum([(x - mean) ** 2 for x in values])
    return (sum_squared_variances / n) ** .5
