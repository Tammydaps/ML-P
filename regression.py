from typing import Union

def mean(values: Union[int, float]) -> float:
    '''
    This function evaluates the mean of `values`
    Args:
        values: Array of numbers
    Returns:
        mean of values (float)
    '''
    return sum(values) / len(values)


def compute_slope(X, Y, X_mean, Y_mean):
    '''
    This particular function computes the slope 'values'
    Args:
       value: Array of numbers
    Returns:
      slope of values(float)
    '''
    numerator = sum((X[i] - X_mean) * (Y[i] - Y_mean) for i in range(len(X)))
    denominator = sum((X[i] - X_mean) ** 2 for i in range(len(X)))
    return numerator / denominator


def compute_intercept(X_mean, Y_mean, slope):
    return Y_mean - (slope * X_mean)
    '''
    This particular function evaluates the intercept 'values'
    Args:
       value: Array of numbers
       Returns:
          intercept of 'values'
    '''
    
def model_fit(X, y):
    mean_x = mean(X)
    mean_y = mean(y)
    slope = compute_slope(X, y, mean_x, mean_y)
    intercept = compute_intercept(mean_x, mean_y, slope)
    return slope, intercept


def model_predict(X, y, X_new):
    intercept, slope = model_fit(X, y)
    return (slope * X_new) + intercept


X = [25, 50, 75, 100, 125, 120, 175, 200]
Y = [5, 10, 15, 20, 25, 30, 35, 40]
X_new = 91

print(model_predict(X, Y, X_new))