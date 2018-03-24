# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:25:05 2018

@author: theresa
"""
import TypeHelper as th

class zipToZCTA:
    ZipCode = 0
    ZCTA = 0
    Neighborhood = ""
    Boro = ""
    
    def __init__(self, zipcd, zcta, nLabel, boro):
        self.ZipCode = th.cleanInts(zipcd)
        self.ZCTA = th.cleanInts(zcta)
        self.Neighborhood = nLabel
        self.Boro = boro
    
    def toStr(self):
        return str(self.ZipCode) + " | " + str(self.ZCTA)