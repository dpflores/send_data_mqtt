import os
import time

path = "/sys/bus/iio/devices/iio:device0/"

# path to Acceleration
pathToAccelX = path + "in_accel_x_raw"
pathToAccelY = path + "in_accel_y_raw"
pathToAccelZ = path + "in_accel_z_raw"
pathToScaleAccel = path + "in_accel_scale"

# Path to Frequency
pathToFrequency = path + "in_accel_sampling_frequency"
pathToAvailableFreq = path + "sampling_frequency_available"

# Constants
g = 9.81 # m/s**2

class Accelerometer:

    def __init__(self):
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.axOff = 0.30476047799999745
        self.ayOff = 0.30476047799999745
        self.azOff = 0.12532269
        self.freq= 0
        self.scale = 0

    def setPrecision(self, range = 4):
        if range == 2:
            scl = 0.002392
        elif range == 4:
            scl = 0.004785
        elif range == 8:
            scl = 0.009581
        elif range == 16:
            scl = 0.019152

        command = "echo " + str(scl) + " > " + pathToScaleAccel
        os.system(command)
        time.sleep(1)

        fileScale  = open(pathToScaleAccel, 'r')
        self.scale = float(fileScale.readline())
        scaleVar = self.scale
        print(f"Precision stablished in +-{range}G with scale={scaleVar}")

    def setSamplingFreq(self, SamplingFreq=125.0):
        
        fileAvailableFreq = open(pathToAvailableFreq, 'r')

        sAvailableFreq = fileAvailableFreq.readline()
        listAvailableFeq = sAvailableFreq.split()
        flotFreqs = [float(fs) for fs in listAvailableFeq]

        if SamplingFreq in flotFreqs:
            command = "echo " + str(SamplingFreq) + " > " + pathToFrequency
            os.system(command)
            time.sleep(1)

            self.freq = float(open(pathToFrequency, 'r').readline())

        else:
            assert("There is no that sampling frequency. Try one of the following frequencies: 15.62, 62.5, 125, 250, 500, 1000, 2000")


    def getSamplingFreq(self):

        self.freq = float(open(pathToFrequency, 'r').readline())

        return self.freq

    def getOffset(self, n_iter = 5000):
        cntOff = 0
        
        # Iterate
        print("Getting offsets. Please, wait a few seconds ...")
        while cntOff < n_iter:
            # Reading files
            fileAx = open(pathToAccelX, 'r')
            fileAy = open(pathToAccelY, 'r')
            fileAz = open(pathToAccelZ, 'r')
            fileScale  = open(pathToScaleAccel, 'r')

            # Getting values
            rawAx = int(fileAx.readline())
            rawAy = int(fileAy.readline())
            rawAz = int(fileAz.readline())
            self.scale = float(fileScale.readline())

            # Scaling values
            self.axOff += rawAx*self.scale
            self.ayOff += rawAy*self.scale
            self.azOff += rawAz*self.scale + g
            
            cntOff += 1
        # Getting offsets
        self.axOff /= n_iter
        self.ayOff /= n_iter
        self.azOff /= n_iter

        print(f"Offset values: ax={self.axOff}, ay={self.axOff}, az={self.azOff}")

    def getAx(self):

        # Reading Files
        fileAx = open(pathToAccelX, 'r')
        fileScale  = open(pathToScaleAccel, 'r')

        # Getting values
        rawAx = int(fileAx.readline())
        self.scale = float(fileScale.readline())
        
        # Getting acceleration in X
        self.ax = rawAx*self.scale - self.axOff

        return self.ax
    
    def getAy(self):

        # Reading Files
        fileAy = open(pathToAccelY, 'r')
        fileScale  = open(pathToScaleAccel, 'r')

        # Getting values
        rawAy = int(fileAy.readline())
        self.scale = float(fileScale.readline())
        
        # Getting acceleration in Y
        self.ay = rawAy*self.scale - self.ayOff

        return self.ay
    
    def getAz(self):

        # Reading Files
        fileAz = open(pathToAccelZ, 'r')
        fileScale  = open(pathToScaleAccel, 'r')

        # Getting values
        rawAz = int(fileAz.readline())
        self.scale = float(fileScale.readline())
        
        # Getting acceleration in Y
        self.az = rawAz*self.scale - self.azOff + g

        return self.az

    def printAccel(self):

        # Acceleration
        fileAccelX = open(pathToAccelX, 'r')
        fileAccelY = open(pathToAccelY, 'r')
        fileAccelZ = open(pathToAccelZ, 'r')
        fileScaleAccel = open(pathToScaleAccel, 'r')

        rawAccelX =  int(fileAccelX.readline())
        rawAccelY =  int(fileAccelY.readline())
        rawAccelZ =  int(fileAccelZ.readline())
        rawAccelScale =  float(fileScaleAccel.readline())
        accelX = rawAccelX*rawAccelScale - self.axOff
        accelY = rawAccelY*rawAccelScale - self.ayOff
        accelZ = rawAccelZ*rawAccelScale + g - self.azOff

        print(accelX, accelY, accelZ)

#dsadqaw
