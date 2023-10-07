import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array([
        [list[0], list[1], list[2]],
        [list[3], list[4], list[5]],
        [list[6], list[7], list[8]],
    ])

    mean = []
    variance = []
    sdt = []
    max = []
    min = []
    sum = []

    for i in range(2):
        mean.append(array.mean(axis = i).tolist())
        variance.append(array.var(axis = i).tolist())
        sdt.append(array.std(axis = i).tolist())
        max.append(array.max(axis = i).tolist())
        min.append(array.min(axis = i).tolist())
        sum.append(array.sum(axis = i).tolist())

    mean.append(array.mean())
    variance.append(array.var())
    sdt.append(array.std())
    max.append(array.max())
    min.append(array.min())
    sum.append(array.sum())
    
    calculations = {"mean": mean,
                    "variance": variance,
                    "standard deviation": sdt,
                    "max": max,
                    "min": min,
                    "sum": sum}
    
    return calculations