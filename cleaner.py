import pandas as pd

LONGITUDE_NAME = ""
LATITUDE_NAME = ""
WORK_ITEM_NAME = ""
WORKLOAD_NAME = ""

def get_X(data):
    if LONGITUDE_NAME not in data.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in data.columns:
        raise ValueError("Check latitude name")
        
    return data.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()

def get_y(data):
    if WORK_ITEM_NAME not in data.columns:
        raise ValueError("Check work item name")
    
    return data.loc[:, [WORK_ITEM_NAME]].to_numpy()

def get_X_test(test_data):
    if LONGITUDE_NAME not in data.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in data.columns:
        raise ValueError("Check latitude name")
        
    return data.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()

def clean(data, test_data):
    X = get_X()
    y = get_y()
    X_test = get_X_test()
    workloads = ["1", "2"]
    
    return (X, y, X_test, workloads)
