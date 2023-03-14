import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"ElementConsumption.xlsx")

availableElements = [["li", "lithium","Lithium"],["beryllium","be","Beryllium"],["vanadium","v","Vanadium"],["iron","fe","Iron"],["nickel","ni","Nickel"],["zinc","zn","Zinc"],["lead","pb","Lead"],["uranium","u","Uranium"]]
xdata = [2013,2014,2015,2016,2017,2018,2019][::-1]
ydata = []
total_lithium=0
total_beryllium=0
total_vanadium=0
total_iron=0
total_nickel=0
total_zinc=0
total_lead=0
total_uranium=0

def predict(year):
    return c + (m * (year))

if __name__=='__main__':
    elements = input("Enter element: ").rstrip().replace(' ','').split(',')

    futureYears = int(input("Enter number of years to predict : "))

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
