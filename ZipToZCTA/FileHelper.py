# -*- coding: utf-8 -*-
"""
@author: Theresa Thomaier
"""
import csv
import re
import pandas as pd

#file reader
def readInCSVDicData(fileName, processFunction):
    fileReader = None
    data = []
    try:
        with open(fileName) as fileReader:
            fileList = csv.DictReader(fileReader) 

            data = processFunction(fileList)
    except IOError as e:
        print("Cound not read in the file at " + fileName + ". Error is: " + str(e))
    except AttributeError as e2:
        print("There was an error: " + str(e2))
    except TypeError as e3:
        print("There was an error: " + str(e3))
    except:
         print("There is a unspecified error.")
    finally:
        if fileReader != None:
            fileReader.close()
            
    return data

def readInCSVData(fileName, processFunction):
    fileReader = None
    data = []
    try:
        with open(fileName) as fileReader:
            fileList = csv.reader(fileReader) 
     
            data = processFunction(fileList)
    except IOError as e:
        print("Cound not read in the file at " + fileName + ". Error is: " + str(e))
    except AttributeError as e2:
        print("There was an error: " + str(e2))
    except TypeError as e3:
        print("There was an error: " + str(e3))
    except:
         print("There is a unspecified error.")
    finally:
        if fileReader != None:
            fileReader.close()
            
    return data

def readInCSVPandas(fileName, index):#, processFunction):
    try:
        if index > -1:
            pData = pd.read_csv(fileName, index_col=index)
        else:
            pData = pd.read_csv(fileName)
            
        #pDataClean = processFunction(pData)
        
    except IOError as e:
        print("Cound not read in the file at " + fileName + ". Error is: " + str(e))
    except AttributeError as e2:
        print("There was an error: " + str(e2))
    except TypeError as e3:
        print("There was an error: " + str(e3))
    except:
         print("There is a unspecified error.")
    
    return pData

def writeOutCSVPandas(fileName, data):
    try:
        data.to_csv(fileName)
    except IOError as e:
        print("Cound not read in the file at " + fileName + ". Error is: " + str(e))
    except AttributeError as e2:
        print("There was an error: " + str(e2))
    except TypeError as e3:
        print("There was an error: " + str(e3))
    except:
         print("There is a unspecified error.")
#user input parsing
def parseToCSVFileName(userInput):
    fullreg = re.compile('^\w+.csv?$')
    csvReg = re.compile('.csv?$')
    
    cleanerInput = userInput.strip()
    
    #if it matches a valid .csv file already, return it
    if re.match(fullreg, cleanerInput):
        return cleanerInput
    
    #if there is a different extention on the file than .csv, kick it out
    if "." in cleanerInput and not re.match(csvReg):
        return "N"
    
    #if there's no extention on it, add the .csv extention and return
    return cleanerInput + ".csv"
    