import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi
from scipy import interpolate 


def sep():

    plt.figure(figsize=(8, 8))
    goes.plot()
    plt.ylabel('FPDO')
    plt.yscale('log')
    plt.show()

    energy = [10, 20, 30, 50, 70, 80]

    plt.figure(figsize=(8, 8))
    plt.plot(np.log(energy),goes.max(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (max)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(np.log(energy),goes.max(),1)
    print("\ndifferential proton flux spectrum (max):  ")
    print(slope_intercept[0])

    f6i = goes['2011-06-03':'2011-06-07']
    fpdo6i = f6i['FPDO_6']
    f6ii = goes['2011-06-09':'2011-06-21']
    fpdo6ii = f6ii['FPDO_6']
    fpdo6i.rolling(3).mean()
    fpdo6ii.rolling(3).mean()

    f5i = goes['2011-06-03':'2011-06-07']
    fpdo5i = f5i['FPDO_5']
    f5ii = goes['2011-06-09':'2011-06-21']
    fpdo5ii = f5ii['FPDO_5']
    fpdo5i.rolling(3).mean()
    fpdo5ii.rolling(3).mean()

    f4i = goes['2011-06-03':'2011-06-05']
    fpdo4i = f4i['FPDO_4']
    f4ii = goes['2011-06-11':'2011-06-21']
    fpdo4ii = f4ii['FPDO_4']
    fpdo4i.rolling(3).mean()
    fpdo4ii.rolling(3).mean()

    f3i = goes['2011-06-03':'2011-06-04']
    fpdo3i = f3i['FPDO_3']
    f3ii = goes['2011-06-18':'2011-06-21']
    fpdo3ii = f3ii['FPDO_3']
    fpdo3i.rolling(3).mean()
    fpdo3ii.rolling(3).mean()

    f2i = goes['2011-06-03':'2011-06-04']
    fpdo2i = f2i['FPDO_2']
    f2ii = goes['2011-06-19':'2011-06-21']
    fpdo2ii = f2ii['FPDO_2']
    fpdo2i.rolling(3).mean()
    fpdo2ii.rolling(3).mean()

    f1i = goes['2011-06-03':'2011-06-04']
    fpdo1i = f1i['FPDO_1']
    f1ii = goes['2011-06-21':'2011-06-21']
    fpdo1ii = f1ii['FPDO_1']
    fpdo1i.rolling(3).mean()
    fpdo1ii.rolling(3).mean()

    plt.figure(figsize=(8, 8))
    plt.plot(np.log(energy),goes.mean(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (mean)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(np.log(energy),goes.mean(),1)
    print("\ndifferential proton flux spectrum (mean):  ")
    print(slope_intercept[0])

    int1 = np.trapz(np.log(energy),goes.max())
    print("\nFPDO max integral : ")
    print(int1)

    int12 = spi.interp1d(np.log(energy),goes.max(), kind='cubic')
    energy_int1 = np.arange(10,80, 2)
    xnew1 = np.log(energy_int1)
    ynew1 = int12(xnew1)
        
    x0= xnew1[0]
    xn = xnew1[-1]
    n = 8

    h = (xn-x0)/n 
    inter1 = int12(x0)  + int12(xn)
    for i in range(1,n):
        k = x0+ i*h
        inter1 = inter1 + 2* int12(k)
    inter1 = inter1 *h/2 
    print("\nFPDO max integral (interpolation): ")
    print(inter1)

    int2 = np.trapz(np.log(energy),goes.mean())
    print("\nFPDO mean integral : ")
    print(int2)

    int22 = interpolate.interp1d(np.log(energy),goes.mean(), kind='cubic')
    energy_int = np.arange(10,80, 2)
    xnew = np.log(energy_int)
    ynew = int22(xnew)
        
    x0= xnew[0]
    xn = xnew[-1]
    n = 8

    h = (xn-x0)/n 
    inter = int22(x0)  + int22(xn)
    for i in range(1,n):
        k = x0+ i*h
        inter = inter + 2* int22(k)
    inter = inter *h/2 

    print("\nFPDO mean integral (interpolation): ")
    print(inter)

    print('\nDatetime of the max values:')
    l = goes.idxmax()
    print(l)

    max= goes.max()
    ar = np.array(max ** 10)
    
    out =[]
    print("\nS NOASS's scale for the max values")
    for i in ar:

        if ( i >= 10^5):
            out.append ("S5")
        elif (( i>= 10^4) &(i < 10^5) ):
            out.append ("S4")
        elif (( i>= 10^3) & (i < 10^4) ):
            out.append ("S3")
        elif ((i < 10^3) &( i>= 10^2)):
            out.append ("S2")
        elif (i <= 10):
            out.append ("S1")
        
    print(out)

    mean= goes.mean()
    arr = np.array(mean ** 10)
    
    out2 =[]
    print("\nS NOASS's scale for the mean values")
    for i in arr:

        if ( i >= 10^5):
            out2.append ("S5")
        elif (( i>= 10^4) &(i < 10^5) ):
            out2.append ("S4")
        elif (( i>= 10^3) & (i < 10^4) ):
            out2.append ("S3")
        elif ((i < 10^3) &( i>= 10^2)):
            out2.append ("S2")
        elif (i <= 10):
            out2.append ("S1")
        
    print(out2)
    
ask = input("Please choose a SEP\n1. 2011-06-03:2011-06-21\n2. 2006-12-06:2006-12-18\n")

if ask in ['1']:

    fname='./SEP_H_GOES13.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2011-06-03':'2011-06-21']
    sep()
elif ask in ['2']:

    fname='./SEP_H_GOES11.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2006-12-06':'2006-12-18']

    sep()
else:
    print("error")
