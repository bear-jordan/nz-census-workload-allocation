# Modules
import pandas as pd
import numpy as np

# Global Variables
## Databases
LONGITUDE_NAME = "Easting"
LATITUDE_NAME = "Northing"
WORK_ITEM_NAME = "Work Item ID"
WORKLOAD_NAME = "SF Workload ID"

## WCATs
LONGITUDE_NAME_NEW = "Easting"
LATITUDE_NAME_NEW = "Northing"
WORK_ITEM_NAME_NEW = "Work Item ID"

# Body
def get_X(data):
    if LONGITUDE_NAME not in data.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in data.columns:
        raise ValueError("Check latitude name")
        
    return data.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()

def get_X_new(newData):
    if LONGITUDE_NAME not in newData.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in newData.columns:
        raise ValueError("Check latitude name")
        
    return newData.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()
    
def get_workitem(data):
    if WORK_ITEM_NAME not in data.columns:
        raise ValueError("Check work item name")
    
    return data.loc[:, [WORK_ITEM_NAME]].to_numpy()
    
def get_workitem_new(newData):
    if WORK_ITEM_NAME_NEW not in newData.columns:
        raise ValueError("Check work item name")
    
    return newData.loc[:, [WORK_ITEM_NAME_NEW]].to_numpy()

def get_workloads(data):
    if WORKLOAD_NAME not in data.columns:
        raise ValueError("Check workload name")
        
    return data.loc[:, [WORKLOAD_NAME]].to_numpy()

def get_resulting_workloads(classifications, data, newData):
    translations = pd.DataFrame({WORKLOAD_NAME: np.ravel(get_workloads(data)), WORK_ITEM_NAME: np.ravel(get_workitem(data))})
    def check_item(item):
        if item not in translations.loc[:, [WORK_ITEM_NAME]].values:
            raise ValueError("Predicted work item not found in the workloads")
    [check_item(item) for item in classifications]
    
    newWorkitems = pd.DataFrame({WORK_ITEM_NAME: np.ravel(get_workitem_new(newData)), "closest": classifications})
    results = pd.merge(newWorkitems, translations, how="left", left_on="closest", right_on="workitem", suffixes=('', '_original'))
    results = results.loc[:, [WORK_ITEM_NAME, WORKLOAD_NAME]]
    
    return results
    

def run_cleaner(data, newData):
    X = get_X(data)
    y = get_workitem(data)
    X_new = get_X_new(newData)
    workloads = get_workloads(data)
    
    return (X, y, X_new, workloads)
