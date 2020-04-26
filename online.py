import numpy as np
import math

data=[]
datanow=[]
datafinal=[]
dataset=[]

label=[]
f1=[]
f2=[]
f3=[]

meanV=[]
stdV=[]
covV=[]

plabelV=[]

n=300
d=3

labelT=[]
fT=[]

def readTest():
    file = open("Test.txt", "r")
    for i in range(0,n):
        data = file.readline()
        datanow = data.split()
        labelT.append(int(datanow[d]))
        
        
def readTrain():
    file = open("Train.txt", "r")
    for i in range(0,n):
        data = file.readline()
        datanow = data.split("\t")
        datanow2 = data.split()
        label.append(int(datanow2[d]))
        datafinal=datanow[0].split()
        f1.append(float(datafinal[0]))
        f2.append(float(datafinal[1]))
        f3.append(float(datafinal[2]))

def plabel():
    for i in range(0,d):
        #print(label.count(i+1))
        plabelV.append(float(label.count(i+1)/n))

def main():
    readTrain()
    meanf1=np.mean(np.array(f1))
    meanf2=np.mean(np.array(f2))
    meanf3=np.mean(np.array(f3))
    stdf1=np.std(np.array(f1))
    stdf2=np.std(np.array(f2))
    stdf3=np.std(np.array(f3))
    meanV.append(meanf1)
    meanV.append(meanf2)
    meanV.append(meanf3)
    stdV.append(stdf1)
    stdV.append(stdf2)
    stdV.append(stdf3)
    x = np.vstack([f1,f2,f3])
    cov = np.cov(x)
    invCov = np.linalg.inv(cov)
    detCov = np.linalg.det(cov)

    plabel()

    #mat = np.matmul(np.subtract(f,meanV).transpose(),invCov,np.subtract(f,meanV))
    #p2=((1/2*3.14)**d)*(detCov**0.5)*np.exp(-.5*np.linalg.det(mat))
    #final=plabelV[1]*p2
    
    print(plabelV)
    print(invCov)
    print(detCov)
    print(meanV)
    print(stdV)
    
main()