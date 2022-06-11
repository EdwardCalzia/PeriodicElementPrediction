import pandas as pd
import xlsxwriter
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_excel(r"C:\Users\edcal\OneDrive\Desktop\Edward\Projects\ElementConsumption.xlsx")
element=input("Enter element: ")
workbook = openpyxl.load_workbook(filename=r"C:\Users\edcal\OneDrive\Desktop\Edward\Projects\ElementConsumption.xlsx")

if element == "Li" or "Lithium" or "lithium":
    print(df.columns[3])
    Lithium=df[df.columns[3]]
    summ=0
    lists=[0,0,0,0,0,0,0]
    years=["2013","2014","2015","2016","2017","2018","2019"]
    for i in range(1,len(Lithium)):
        print(Lithium[i])
        summ+=Lithium[i]
        lists[i-1]+=Lithium[i]
    average=summ/len(Lithium)
    print(average)
    print(lists)


    def best_fit(X, Y):
        
        xbar = average
        ybar = 2016
        n = len(X) # or len(Y)

        numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
        denum = sum([xi**2 for xi in X]) - n * xbar**2

        b = numer / denum
        a = ybar - b * xbar

        print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

        return a, b

    a, b = best_fit(years, lists)
    plt.scatter(years, lists)
    yfit = [a + b * xi for xi in years]
    plt.plot(X, yfit)
    plt.show()





