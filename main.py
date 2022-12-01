import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 


def sep():

    plt.figure(figsize=(8, 8))
    goes.plot()
    plt.ylabel('FPDO')
    plt.yscale('log')
    plt.show()

    energy = [6.643, 12.61, 20.55, 46.62, 103.7, 154.6] 

    eimax =  interpolate.interp1d(energy,goes.max()**10)
    exnew = np.array(np.arange(10,80,0.1))
    e = eimax(exnew)
    plt.plot(exnew, e)
    plt.xlabel("energy(MeV)")
    plt.ylabel("FPDO")
    plt.title("1d Interpolation (max)")
    #plt.show()
    print("differential proton flux spectrum (max):\n 10 MeV: ",eimax(10),"\n 30 MeV: ",eimax(30),"\n 80 Mev: ",eimax(80),"\n\n")

    eimean =  interpolate.interp1d(energy,goes_all_m[:,0]**10)
    en = eimean(exnew)
    plt.plot(exnew, en)
    plt.xlabel("energy(MeV)")
    plt.ylabel("FPDO")
    plt.title("1d Interpolation (mean)")
    #plt.show()
    print("differential proton flux spectrum (mean):\n 10 MeV: ",eimean(10),"\n 30 MeV: ",eimean(30),"\n 80 Mev: ",eimean(80),"\n\n")

    plt.figure(figsize=(8, 8))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (max)')  
    plt.loglog(energy,goes.max()**10)
    #plt.show()

    
    slope_intercept10max = np.polyfit(np.log10(exnew[0:9]),np.log10(eimax(exnew[0:9]) ),1)
    slope_intercept30max = np.polyfit(np.log10(exnew[200:209]),np.log10(eimax(exnew[200:209]) ),1)
    slope_intercept80max = np.polyfit(np.log10(exnew[690:699]),np.log10(eimax(exnew[690:699]) ),1)

    slope_intercept10mean = np.polyfit(np.log10(exnew[0:9]),np.log10(eimean(exnew[0:9]) ),1)
    slope_intercept30mean = np.polyfit(np.log10(exnew[200:209]),np.log10(eimean(exnew[200:209]) ),1)
    slope_intercept80mean = np.polyfit(np.log10(exnew[690:699]),np.log10(eimean(exnew[690:699]) ),1)


    z = np.array(np.exp(slope_intercept10max[1]) * (energy ** slope_intercept10max[0]))      #power law y = b*x^a
    int10x = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[3]
    xn = xnew1[4]
    n = 17

    h = (xn-x0)/n      
    
    inter10max = int10x(x0)  + int10x(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter10max = inter10max + 2* int10x(k)
    inter10max = inter10max *h/2 

    z = np.array(np.exp(slope_intercept30max[1]) * (energy ** slope_intercept30max[0]))      #power law y = b*x^a
    int30x = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[23]
    xn = xnew1[24]
    n = 17

    h = (xn-x0)/n      
    
    inter30max = int30x(x0)  + int30x(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter30max = inter30max + 2* int30x(k)
    inter30max = inter30max *h/2 

    z = np.array(np.exp(slope_intercept80max[1]) * (energy ** slope_intercept80max[0]))      #power law y = b*x^a
    int80x = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[73]
    xn = xnew1[74]
    n = 17

    h = (xn-x0)/n      
    
    inter80max = int80x(x0)  + int80x(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter80max = inter80max + 2* int80x(k)
    inter80max = inter80max *h/2 
    print("\nFPDO max integral (power law):\n 10 Mev:",inter10max**10,"\n 30 Mev: ",inter30max**10,"\n 80 Mev: ",inter80max**10,"\n\n")
   

    z = np.array(np.exp(slope_intercept10mean[1]) * (energy ** slope_intercept10mean[0]))      #power law y = b*x^a
    int10n = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[3]
    xn = xnew1[4]
    n = 17

    h = (xn-x0)/n      
    
    inter10mean = int10n(x0)  + int10n(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter10mean = inter10mean + 2* int10n(k)
    inter10mean = inter10mean *h/2 


    z = np.array(np.exp(slope_intercept30mean[1]) * (energy ** slope_intercept30mean[0]))      #power law y = b*x^a
    int30n = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[23]
    xn = xnew1[24]
    n = 17

    h = (xn-x0)/n      
    
    inter30mean = int30n(x0)  + int30n(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter30mean = inter30mean + 2* int30n(k)
    inter30mean = inter30mean *h/2 

    z = np.array(np.exp(slope_intercept80mean[1]) * (energy ** slope_intercept80mean[0]))      #power law y = b*x^a
    int80n = interpolate.interp1d(np.log10(energy),np.log10(z))

    energy_int1 = np.arange(7, 154.6, 1)
    xnew1 = np.array(np.log10(energy_int1))

    x0= xnew1[73]
    xn = xnew1[74]
    n = 17

    h = (xn-x0)/n      
    
    inter80mean = int80n(x0)  + int80n(xn)
    for i in range(1,n):
        k = x0+ i*h
       
        inter80mean = inter80mean + 2* int80n(k)
    inter80mean = inter80mean *h/2 
    print("\nFPDO mean integral (power law):\n 10 Mev:",inter10mean**10,"\n 30 Mev: ",inter30mean**10,"\n 80 Mev: ",inter80mean**10,"\n\n")
    
    plt.figure(figsize=(8, 8))
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.ylabel('FPDO')
    plt.xlabel('Energy')
    plt.title('SPE differential proton flux spectrum (mean)')
    plt.loglog(energy,goes_all_m**10)
    #plt.show()

    int10max = np.trapz(np.log10(eimax(exnew[0:9])),np.log10(eimax(exnew[0:9]) ))
    int30max = np.trapz(np.log10(eimax(exnew[200:209])),np.log10(eimax(exnew[200:209]) ))
    int80max = np.trapz(np.log10(eimax(exnew[690:699])),np.log10(eimax(exnew[690:699]) ))
    print("\nFPDO max integral :\n 10 Mev:",int10max**10,"\n 30 Mev:",int30max**10,"\n 80 MeV",int80max**10,"\n\n")

    int10mean = np.trapz(np.log10(eimean(exnew[0:9])),np.log10(eimean(exnew[0:9]) ))
    int30mean = np.trapz(np.log10(eimean(exnew[200:209])),np.log10(eimean(exnew[200:209]) ))
    int80mean = np.trapz(np.log10(eimean(exnew[690:699])),np.log10(eimean(exnew[690:699]) ))
    print("\nFPDO mean integral :\n 10 Mev:",int10mean**10,"\n 30 Mev:",int30mean**10,"\n 80 MeV",int80mean**10,"\n\n")


    print('\nDatetime of the max values:')
    l = goes.idxmax()
    print(l)

    max= goes.max()
    ar = np.array(max ** 10)
    
    out =[]
    print("\nS NOASS's scale for the max values")
    

    if ( eimax(10) >= 10^5):
        out.append ("S5")
    elif (( eimax(10)>= 10^4) &(eimax(10) < 10^5) ):
        out.append ("S4")
    elif (( eimax(10) >= 10^3) & (eimax(10) < 10^4) ):
        out.append ("S3")
    elif ((eimax(10) < 10^3) &( eimax(10) >= 10^2)):
        out.append ("S2")
    elif (eimax(10) <= 10):
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

    goes = goes['2006-12-12':'2006-12-18']

    mask1 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask12 = goes['2006-12-17':'2006-12-18'].rolling(3).mean()
    mask13 = goes['2006-12-13':'2006-12-17']

    mask = pd.concat ([mask1,mask12,mask13])
    tmask = pd.DataFrame(mask, columns=['FPDO_1'])

    mask2 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask22 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask23 = goes['2006-12-13':'2011-06-16']

    mask2 = pd.concat ([mask2,mask22,mask23])
    tmask2 = pd.DataFrame(mask2, columns=['FPDO_2'])

    mask3 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask32 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask33 = goes['2006-12-13':'2006-12-16']

    mask3 = pd.concat ([mask3,mask32,mask33])
    tmask3 = pd.DataFrame(mask3, columns=['FPDO_3'])

    mask4 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask42 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask43 = goes['2006-12-13':'2006-12-16']

    mask4 = pd.concat ([mask4,mask42,mask43])
    tmask4 = pd.DataFrame(mask4, columns=['FPDO_4'])

    mask5 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask52 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask53 = goes['2006-12-13':'2006-12-16']

    mask5 = pd.concat ([mask5,mask52,mask53])
    tmask5 = pd.DataFrame(mask5, columns=['FPDO_5'])

    mask6 = goes['2006-12-12':'2006-12-13'].rolling(3).mean()
    mask62 = goes['2006-12-16':'2006-12-18'].rolling(3).mean()
    mask63 = goes['2006-12-13':'2006-06-16']

    mask6= pd.concat ([mask6,mask62,mask63])
    tmask6 = pd.DataFrame(mask6, columns=['FPDO_6'])

    
    goes_all = [tmask.mean(),tmask2.mean(),tmask3.mean(),tmask4.mean(),tmask5.mean(),tmask6.mean()]
    goes_all_m = np.array(goes_all)


    sep()

else:
    print("error")
