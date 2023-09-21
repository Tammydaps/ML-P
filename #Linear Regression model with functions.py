#Linear Regression model with functions 
#calculating the mean of a list of values
def mean(values):
    return sum(values) / len(values)

#calculating the slope of a regresion line
#slope(m) = incremental change in Y / incremental change in X
def compute_slope(X, Y, X_mean, Y_mean):
    numerator = sum((X[i] - X_mean) * (Y[i] - Y_mean) for i in range(len(X)))
    denominator = sum((X[i] - X_mean) ** 2 for i in range(len(X)))
    return numerator / denominator

#Now lets write a function to compute the intercept (b) of a regression line
#the points wehrer the regression line cuts both axis
def compute_intercept(X_mean, Y_mean, slope):
    return Y_mean - (slope * X_mean)

#Now lets write a function to make predictions 
def predict(X_new, slope, intercept):
    return (slope * X_new) + intercept

#But we actually need a sample data. lets use;
X = [25, 50, 75, 100, 125, 150, 175, 200]
Y = [5, 10, 15, 20, 25, 30, 35, 40]

#We can now compute the mean values X and Y respectively but we have to define theese variables 
X_mean = mean(X)
Y_mean = mean(Y)

#kindly compute the slope and intercept 
slope = compute_slope(X, Y, X_mean, Y_mean)
intercept = compute_intercept(X_mean, Y_mean, slope)

#Now it's time to predict a new value 
X_new = 225
Y_pred = predict(X_new, slope, intercept)

print(f"predicted value for X_new={X_new}: {Y_pred}")