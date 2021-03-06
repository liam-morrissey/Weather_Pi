import time
import adcUtil as adc
from os import path
#TODO edit anything with a TODO

#~~~~~~~~~~~~~~~~~~~~Assignment~~~~~~~~~~~~~~~~~~~~~~~~~~~~

location = "GOLDEN" #TODO Change me based on location
fName = location+"_data.csv" #set up the file name 

tChan = (0,0)#Channel 0, chip 0 Temperature
lChan = (1,0)#Channel 1, chip 0 Light
aChan = (0,1)#Channel 0,  chip 1 Audio
eChan = (1,1)#Channel 1,  chip 1 Envelope

#~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def readTemp():#Read thermometer
    tmp = adc.readADC(tChan[0],tChan[1])
    return (100*tmp -50) #Change Volts to deg. C

def readAud():#Read Audio
    return (adc.readADC(aChan[0],aChan[1])-1.65) #-1.65 to adjust audio voltage to 0

def readEnv():#Read Audio Envelope
    return adc.readADC(eChan[0],eChan[1])

def readLight():#Read Photoresistor
    return adc.readADC(lChan[0],lChan[1])

#~~~~~~~~~~~~~~~~~~~~Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tmp = ("{:.3f},".format(readTemp())+#Record Temperature
        "{:.3f},".format(readLight())+#Record Light
        "{:.3f},".format(readAud())+#Record Audio
        "{:.3f},".format(readEnv())+#Record Audio Envelope
       "{:.0f}".format(time.time()))#Record time in epoch UTC


flag=False
if(not path.exists(fName)):#prints the header if the file does not exist
    flag=True

with open(fName,'a') as f: #open up the file in append mode
    if(flag):print("Temp,Light,Audio,AudioEnv,Time",file=f)#print header

    print(tmp, file=f)#print this in the file
    f.close()

print("Data Collected")
