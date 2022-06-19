import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\edcal\OneDrive\Desktop\Edward\Projects\ElementConsumption.xlsx")

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

    if "li" in elements:
        for i in range(0,futureYears):
            total_lithium+=predict(i+2022)         

            if total_lithium >= 14000000:
                print("Lithium will run out in " + str(i+2022))
                break
            else:
                pass

    if "be" in elements:
        for i in range(0,futureYears):
            total_beryllium+=predict(i+2022)

            if total_beryllium >= 400000:
                print("Beryllium will run out in " + str(i+2022))
                break
            else:
                pass

    if "v" in elements:
        for i in range(0,futureYears):
            total_vanadium+=predict(i+2022)

            if total_vanadium >= 63000000:
                print("Vanadium will run out in " + str(i+2022))
                break
            else:
                pass

    if "fe" in elements:
        for i in range(0,futureYears):
            total_iron+=predict(i+2022)

            if total_iron >= 85000000000:
                print("Iron will run out in " + str(i+2022))
                break
            else:
                pass

    if "ni" in elements:
        for i in range(0,futureYears):
            total_nickel+=predict(i+2022)

            if total_nickel >= 300000000:
                print("Nickel will run out in " + str(i+2022))
                break
            else:
                pass

    if "zn" in elements:
        for i in range(0,futureYears):
            total_zinc+=predict(i+2022)

            if total_zinc >= 250000000:
                print("Zinc will run out in " + str(i+2022))
                break
            else:
                pass

    if "pb" in elements:
        for i in range(0,futureYears):
            total_lead+=predict(i+2022)

            if total_lead >= 90400000:
                print("Lead will run out in " + str(i+2022))
                break
            else:
                pass

    if "u" in elements:
        for i in range(0,futureYears):
            total_uranium+=predict(i+2022)

            if total_uranium >= 16000000:
                print("Uranium will run out in " + str(i+2022))
                break
            else:
                pass
    plt.show()
