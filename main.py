import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 
import math


def sep():

    plt.figure(figsize=(8, 8))
    goes.plot()
    plt.ylabel('FPDO')
    plt.yscale('log')
    #plt.show()

    energy = [6.643, 12.61, 20.55, 46.62, 103.7, 154.6] 

    plt.figure(figsize=(8, 8))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (max)')  
    plt.loglog(energy,goes.max()**10)
    #plt.show()

    slope_intercept = np.polyfit(np.log10(energy),np.log10(goes.max()),1)
    print("\ndifferential proton flux spectrum (max):  ")
    print(slope_intercept[0]**10)

    
    plt.figure(figsize=(8, 8))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (mean)')
    plt.loglog(energy,goes_all_m**10)
    #plt.show()

    slope_intercept1 = np.polyfit(np.log10(energy),np.log(goes_all_m[:,0]),1)
    print("\ndifferential proton flux spectrum (mean):  ")
    print(slope_intercept1[0]**10)

    int1 = np.trapz(np.log10(energy),np.log10(goes.max()))
    print("\nFPDO max integral : ")
    print(int1**10)

    z = (goes.max() ** 10)
    z = np.array(np.exp(slope_intercept[1]) * (energy ** slope_intercept[0]))      #power law y = b*x^a
    int12 = interpolate.interp1d(np.log10(energy),np.log10(z), kind='cubic')

    energy_int1 = np.arange(6.643, 154.6, 2)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[0]
    xn = xnew1[-1]
    n = 17

    h = (xn-x0)/n      
    
    inter1 = int12(x0)  + int12(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter1 = inter1 + 2* int12(k)
    inter1 = inter1 *h/2 
    print("\nFPDO max integral (interpolation): ")
    print(inter1**10)

    int2 = np.trapz(np.log10(energy),np.log10(goes_all_m[:,0]))
    print("\nFPDO mean integral : ")
    print(int2**10)

    t = (goes_all_m[:,0] ** 10)
    t = np.array(np.exp(slope_intercept1[1]) * (energy ** slope_intercept1[0]))      #power law y = b*x^a
    int22 = interpolate.interp1d(np.log10(energy),np.log10(t), kind='cubic')

    energy_int = np.arange(6.643, 154.6, 2)
    xnew = np.array(np.log10(energy_int))

    x0= xnew[0]
    xn = xnew[-1]
    n = 17

    h = (xn-x0)/n      
    
    inter = int22(x0)  + int22(xn)
    for i in range(1,n):
        k = x0+ i*h
        
        inter = inter + 2* int22(k)
    inter = inter *h/2 
    print("\nFPDO mean integral (interpolation): ")
    print(inter**10)


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
    
    
ask = input("Please choose a SEP\n1. 2011-06-03:2011-06-21\n2. 2006-12-06:2006-12-18\n")

if ask in ['1']:

    fname='./SEP_H_GOES13.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2011-06-03':'2011-06-21']

    mask1 = goes['2011-06-03':'2011-06-04'].rolling(3).mean()
    mask12 = goes['2011-06-21':'2011-06-21'].rolling(3).mean()
    mask13 = goes['2011-06-04':'2011-06-21']

    mask = pd.concat ([mask1,mask12,mask13])
    tmask = pd.DataFrame(mask, columns=['FPDO_1'])

    mask2 = goes['2011-06-03':'2011-06-04'].rolling(3).mean()
    mask22 = goes['2011-06-19':'2011-06-21'].rolling(3).mean()
    mask23 = goes['2011-06-04':'2011-06-19']

    mask2 = pd.concat ([mask2,mask22,mask23])
    tmask2 = pd.DataFrame(mask2, columns=['FPDO_2'])

    mask3 = goes['2011-06-03':'2011-06-04'].rolling(3).mean()
    mask32 = goes['2011-06-18':'2011-06-21'].rolling(3).mean()
    mask33 = goes['2011-06-04':'2011-06-18']

    mask3 = pd.concat ([mask3,mask32,mask33])
    tmask3 = pd.DataFrame(mask3, columns=['FPDO_3'])

    mask4 = goes['2011-06-03':'2011-06-05'].rolling(3).mean()
    mask42 = goes['2011-06-11':'2011-06-21'].rolling(3).mean()
    mask43 = goes['2011-06-05':'2011-06-11']

    mask4 = pd.concat ([mask4,mask42,mask43])
    tmask4 = pd.DataFrame(mask4, columns=['FPDO_4'])

    mask5 = goes['2011-06-03':'2011-06-07'].rolling(3).mean()
    mask52 = goes['2011-06-09':'2011-06-21'].rolling(3).mean()
    mask53 = goes['2011-06-07':'2011-06-09']

    mask5 = pd.concat ([mask5,mask52,mask53])
    tmask5 = pd.DataFrame(mask5, columns=['FPDO_5'])

    mask6 = goes['2011-06-03':'2011-06-07'].rolling(3).mean()
    mask62 = goes['2011-06-09':'2011-06-21'].rolling(3).mean()
    mask63 = goes['2011-06-07':'2011-06-09']

    mask6= pd.concat ([mask6,mask62,mask63])
    tmask6 = pd.DataFrame(mask6, columns=['FPDO_6'])

    
    goes_all = [tmask.mean(),tmask2.mean(),tmask3.mean(),tmask4.mean(),tmask5.mean(),tmask6.mean()]
    goes_all_m = np.array(goes_all)

    sep()
elif ask in ['2']:

    fname='./SEP_H_GOES11.txt'
    colnames=['epoch', 'FPDO_1', 'FPDO_2','FPDO_3','FPDO_4','FPDO_5','FPDO_6'] 

    goes=pd.read_csv(fname,sep=',',skiprows=1,names=colnames,header=None)
    goes['epoch']=pd.to_datetime(goes['epoch'])
    goes  = goes.set_index('epoch')   

    goes = goes['2006-12-06':'2006-12-18']

    mask1 = goes['2006-12-06':'2006-12-06'].rolling(3).mean()
    mask12 = goes['2006-12-17':'2006-12-18'].rolling(3).mean()
    mask13 = goes['2006-12-06':'2006-12-17']

    mask = pd.concat ([mask1,mask12,mask13])
    tmask = pd.DataFrame(mask, columns=['FPDO_1'])

    mask2 = goes['2006-12-06':'2006-12-06'].rolling(3).mean()
    mask22 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask23 = goes['2006-12-06':'2011-06-16']

    mask2 = pd.concat ([mask2,mask22,mask23])
    tmask2 = pd.DataFrame(mask2, columns=['FPDO_2'])

    mask3 = goes['2006-12-06':'2006-12-06'].rolling(3).mean()
    mask32 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask33 = goes['2006-12-06':'2006-12-16']

    mask3 = pd.concat ([mask3,mask32,mask33])
    tmask3 = pd.DataFrame(mask3, columns=['FPDO_3'])

    mask4 = goes['2006-12-06':'2006-12-06'].rolling(3).mean()
    mask42 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask43 = goes['2006-12-06':'2006-12-16']

    mask4 = pd.concat ([mask4,mask42,mask43])
    tmask4 = pd.DataFrame(mask4, columns=['FPDO_4'])

    mask5 = goes['2006-12-06':'2006-12-07'].rolling(3).mean()
    mask52 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask53 = goes['2006-12-07':'2006-12-16']

    mask5 = pd.concat ([mask5,mask52,mask53])
    tmask5 = pd.DataFrame(mask5, columns=['FPDO_5'])

    mask6 = goes['2006-12-06':'2006-12-07'].rolling(3).mean()
    mask62 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask63 = goes['2006-12-07':'2006-06-16']

    mask6= pd.concat ([mask6,mask62,mask63])
    tmask6 = pd.DataFrame(mask6, columns=['FPDO_6'])

    
    goes_all = [tmask.mean(),tmask2.mean(),tmask3.mean(),tmask4.mean(),tmask5.mean(),tmask6.mean()]
    goes_all_m = np.array(goes_all)


    sep()

else:
    print("error")
