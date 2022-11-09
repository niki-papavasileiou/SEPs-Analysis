import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def firstsep():

    fname='./SEP_H_GOES13.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2011-06-03':'2011-06-22']


    plt.figure(figsize=(8, 8))
    goes.plot()
    plt.ylabel('FPDO')
    plt.yscale('log')
    plt.show()

    energy = [10,20, 30,50, 70, 80]

    plt.figure(figsize=(8, 8))
    plt.plot(energy,goes['2011-06-03':'2011-06-22'].max(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (max)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(energy,goes['2011-06-03':'2011-06-22'].max(),1)
    print("\ndifferential proton flux spectrum (max):  ")
    print(slope_intercept[0])

    goes['FPDO_1'].rolling(window =20).mean().plot()
    goes['FPDO_2'].rolling(window =20).mean().plot()
    goes['FPDO_3'].rolling(window =20).mean().plot()
    goes['FPDO_4'].rolling(window =20).mean().plot()
    goes['FPDO_5'].rolling(window =20).mean().plot()
    goes['FPDO_6'].rolling(window =20).mean().plot()

#0.0001-0.08

    plt.figure(figsize=(8, 8))
    plt.plot(energy,goes['2011-05-02':'2011-06-29'].median(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (med)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(energy,goes['2011-06-03':'2011-06-22'].median(),1)
    print("\ndifferential proton flux spectrum (median):  ")
    print(slope_intercept[0])

    int1 = np.trapz(energy, goes['2011-05-02':'2011-06-29'].max())
    print("\nFPDO max integral: ")
    print(int1)

    int2 = np.trapz(energy, goes['2011-05-02':'2011-06-29'].median())
    print("\nFPDO median integral: ")
    print(int2)

    print('\nDatetime of the max values:')
    l = goes['2011-05-02':'2011-06-29'].idxmax()
    print(l)


    max= goes['2011-05-02':'2011-06-29'].max()

    i =0 
    print("\nS NOASS's scale for the max values")
    for i in max:

        if ((i < 10^6) &( i >= 10^5)):
            print ('S5')
        elif ((i < 10^5) &( i>= 10^4)):
            print ('S4')
        elif ((i < 10^4) &( i>= 10^3)):
            print ('S3')
        elif ((i < 10^3) &( i>= 10^2)):
            print ('S2')
        elif i <= 10:
            print ('S1')

    median = goes['2011-05-02':'2011-06-29'].median()

    j =0 
    print("\nS NOASS's scale for the median values ")
    for j in median:

        if ((j < 10^6) &( j >= 10^5)):
            print ('S5')
        elif ((j < 10^5) &( j>= 10^4)):
            print ('S4')
        elif ((j < 10^4) &( j>= 10^3)):
            print ('S3')
        elif ((j < 10^3) &( j>= 10^2)):
            print ('S2')
        elif j <= 10:
            print ('S1')


def secsep():

    fname='./SEP_H_GOES11.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2006-11-30':'2006-12-21']


    plt.figure(figsize=(8, 8))
    goes.plot()
    plt.ylabel('FPDO')
    plt.yscale('log')
    plt.show()

    energy = [10,20, 30,50, 70, 80]

    plt.figure(figsize=(8, 8))
    plt.plot(energy,goes['2006-11-30':'2006-12-21'].max(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (max)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(energy,goes['2006-11-30':'2006-12-21'].max(),1)
    print("\ndifferential proton flux spectrum (max):  ")
    print(slope_intercept[0])

    goes['FPDO_1'].rolling(window =20).mean().plot()
    goes['FPDO_2'].rolling(window =20).mean().plot()
    goes['FPDO_3'].rolling(window =20).mean().plot()
    goes['FPDO_4'].rolling(window =20).mean().plot()
    goes['FPDO_5'].rolling(window =20).mean().plot()
    goes['FPDO_6'].rolling(window =20).mean().plot()


    plt.figure(figsize=(8, 8))
    plt.plot(energy,goes['2006-11-30':'2006-12-21'].median(),'o-')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (med)')
    plt.yscale('log')
    plt.show()

    slope_intercept = np.polyfit(energy,goes['2006-11-30':'2006-12-21'].median(),1)
    print("\ndifferential proton flux spectrum (max):  ")
    print(slope_intercept[0])


    int1 = np.trapz(energy, goes['2006-11-30':'2006-12-21'].max())
    print("\nFPDO max integral: ")
    print(int1)

    int2 = np.trapz(energy, goes['2006-11-30':'2006-12-21'].median())
    print("\nFPDO median integral: ")
    print(int2)


    print('\nDatetime of the max values:\n')
    l = goes['2006-11-30':'2006-12-21'].idxmax()
    print(l)


    max= goes['2006-11-30':'2006-12-21'].max()

    i =0 
    print("\nS NOASS's scale for the max values\n ")
    for i in max:

        if ((i < 10^6) &( i >= 10^5)):
            print ('S5')
        elif ((i < 10^5) &( i>= 10^4)):
            print ('S4')
        elif ((i < 10^4) &( i>= 10^3)):
            print ('S3')
        elif ((i < 10^3) &( i>= 10^2)):
            print ('S2')
        elif i <= 10:
            print ('S1')

    median = goes['2006-11-30':'2006-12-21'].median()

    j =0 
    print("\nS NOASS's scale for the median values \n")
    for j in median:

        if ((j < 10^6) &( j >= 10^5)):
            print ('S5')
        elif ((j < 10^5) &( j>= 10^4)):
            print ('S4')
        elif ((j < 10^4) &( j>= 10^3)):
            print ('S3')
        elif ((j < 10^3) &( j>= 10^2)):
            print ('S2')
        elif j <= 10:
            print ('S1')


ask = input("Please choose a SEP\n1. 2011-06-03:2011-06-22\n2. 2006-11-30:2006-12-21\n")

if ask in ['1']:

    firstsep()
elif ask in ['2']:
    secsep()
else:
    print("error")
