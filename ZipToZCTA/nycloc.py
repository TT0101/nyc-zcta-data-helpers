# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 18:56:21 2018

@author: theresa
"""
import FileHelper as fh
import TypeHelper as th
import ziptozcta as zz


def LoadZipToZCTA():
    fileName = r'Datafiles/zip_to_zcta10_nyc_with_NBH.csv'
    return fh.readInCSVDicData(fileName, processZipToZCTA)
    
#def LoadZCTAToTract():
#    fileName = r'zcta_tract_rel_10.csv'
#    return fh.readInCSVDicData(fileName, processZCTAToTract)
#    
#def LoadTractToNTA():
#    fileName = r'CensusToNTA.csv'
#    return fh.readInCSVDicData(fileName, processTractToNTA)

#process
def processZipToZCTA(fileList):
    data = []
    #rowCount = 0
    for line in fileList:
        obj = zz.zipToZCTA(line['zipcode'].strip(), line['zcta5'].strip(), line['neighborhoodlabel'].strip(), line['boro'].strip())
        data.append(obj)            
        #rowCount += 1
    
    return data

#def processZCTAToTract(fileList):#fix these when classes set up
#    data = []
#    #rowCount = 0
#    for line in fileList:
#        obj = zt.ZCTAToTract(line['ZCTA5'].strip(), line['TRACT'].strip(), line['ZAREAPCT'], line['TRAREAPCT'])
#        data.append(obj)            
#        #rowCount += 1
#    
#    return data
#    
#def processTractToNTA(fileList):
#    data = []
#    #rowCount = 0
#    for line in fileList:
#        obj = line#zz.zipToZCTA(line['zipcode'].strip(), line['zcta5'].strip())
#        data.append(obj)            
#        #rowCount += 1
#    
#    return data

#get
def getZCTAByZip(zipCode, data):
    try:
        print("zipcode from file: " + str(zipCode))
        matching = [item for item in data if item.ZipCode == zipCode]
        
        if(len(matching) > 0):
            print("found match" + str(matching[0].ZCTA))
            return matching[0]
        
        print("no match")
        return zz.zipToZCTA(0, 0, '', '') #return blank one so no error occurrs, just dumps a 0 in the file
    
    except Exception as e:
        print("Error: " + str(e))

#use this to just get the zcta.  less efficent since have to get the data every call
def getZCTAValueByZip(zipCode):
    data = LoadZipToZCTA()
    obj = getZCTAByZip(zipCode, data)
    if(obj == None):
        return obj
    else:
        return obj.ZCTA

#uses file from run input to append data to file.
def appendZCTADataToFile(fileFrame, zipcol):
    mapdata = LoadZipToZCTA()
    field1 = 'zcta'
    field2 = 'nbhLabel'
    field3 = 'boroLabel'
    
    fileFrame[field1] = fileFrame[zipcol].apply(lambda x: getZCTAByZip(th.cleanInts(x), mapdata).ZCTA)
    fileFrame[field2] = fileFrame[zipcol].apply(lambda x: getZCTAByZip(th.cleanInts(x), mapdata).Neighborhood)
    fileFrame[field3] = fileFrame[zipcol].apply(lambda x: getZCTAByZip(th.cleanInts(x), mapdata).Boro)
    
    return fileFrame

def run():
    #print(getZCTAByZip(10001, zipToZCTAFile))
    
    inText = input("Enter the name of the file to add zcta data to (or enter 'exit' to exit): ")
    if inText.upper() != 'EXIT':
        
        fileName = fh.parseToCSVFileName(inText)
            
        if fileName == 'N':
            print("Invalid file name was provided, please try again.")
        else:
            print("Attempting to read data...\n")
            data = fh.readInCSVPandas(fileName, -1)
            
            zipCol = input("What column contains the zip code (name label)? ")
            
            fh.writeOutCSVPandas("withZCTA_" + fileName, appendZCTADataToFile(data, zipCol)) 
            
            print("Done.")

#run
run()
