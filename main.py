import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"ElementConsumption.xlsx")

availableElements = [["li", "lithium","Lithium"],["beryllium","be","Beryllium"],["vanadium","v","Vanadium"]]
xdata = [2013,2014,2015,2016,2017,2018,2019][::-1]
ydata = []
futureYears = 5

def predict(year):
    return c + (m * (year))

if __name__=='__main__':
    elements = input("Enter elements (separate with comma) : ").rstrip().replace(' ','').split(',')

    for element in elements:
        for availableElement in availableElements:
            if element.lower() in availableElement:
                ydata.append(df.loc[:,availableElement[2]])
                break

    for ydataI in ydata:
        sumx = sum(xdata)
        sumy = sum(ydataI)
        sumx2 = sum([x**2 for x in xdata])
        sumy2 = sum([y**2 for y in ydataI])
        sumxy = sum([x*y for x,y in zip(xdata, ydataI)])
        n = len(xdata)

        m = ((n*sumxy)-(sumx*sumy))/((n*sumx2)-(sumx**2))
        c = (sumy - (m * sumx))/n

        linedataX = np.linspace(min(xdata),max(xdata)+futureYears, 100)
        linedataY = c + (m * linedataX)

        plt.scatter(xdata, ydataI)
        plt.plot(linedataX, linedataY)

    plt.show()