# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:52:19 2021

@author: sun jae yoon
"""
import json

bdays = []

def readThru(file):
    lines = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.find('birthdate') > 0:
                lines.append(line)
                
    return lines



def recursiveSearchDict(tree):
    if type(tree) == dict:
        #if 'birthdate' in tree.keys():
        if len(tree) == 17:
            bdays.append(tree)
            return
        else:
            for key in tree:
                recursiveSearchDict(tree[key])

    elif type(tree) == list:
        recursiveSearchList(tree)
        
    else:
        return
    
def recursiveSearchList(tree):

    if type(tree) == list:
        for key in tree:
            recursiveSearchList(key)
            
    elif type(tree) == dict:
        recursiveSearchDict(tree)
        
    else:
        return
    
    
def getBdays(data): 
    global bdays 
    data1 = [string for string in data.split('(') if string.find("birthdate")>=0][0]
    data1 = [string for string in data1.split(')') if string.find("birthdate")>=0][0]

    res = json.loads(data1.strip().strip("ScheduledApplyEach, "))#['require']
    recursiveSearchList(res)
    return bdays


    



            
            