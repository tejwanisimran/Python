import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    # load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : X - ",X)
    print("Values of Dependent Variables : Y - ",Y)

    # Calculating mean/average
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is : ",mean_x)        # 3.0
    print("Y_MEAN is : ",mean_y)        # 3.6

    n = len(X)      # 5

    # Y = mX + C
    # m = (summation(x - x-bar)(y - y-bar)) / (summation(x - x-bar) ** 2))

    # Calculating slope i.e m
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)
  
    m = numerator / denominator

    print("Slope of line is : m -",m)       # 0.4

    # Calculating C i.e Y-intercept
    C = mean_y - (m * mean_x)

    print("Y intercept is : C - ",C)  

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()