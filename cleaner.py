import pandas as pd

LONGITUDE_NAME = "longitude"
LATITUDE_NAME = "latitude"
WORK_ITEM_NAME = "workitem"
WORKLOAD_NAME = "workload"

LONGITUDE_NAME_NEW = "longitude"
LATITUDE_NAME_NEW = "latitude"
WORK_ITEM_NAME_NEW = "workitem"

def get_X(data):
    if LONGITUDE_NAME not in data.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in data.columns:
        raise ValueError("Check latitude name")
        
    return data.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()

def get_X_new(newData):
    if LONGITUDE_NAME not in data.columns:
        raise ValueError("Check longitude name")
    if LATITUDE_NAME not in data.columns:
        raise ValueError("Check latitude name")
        
    return data.loc[:, [LATITUDE_NAME, LONGITUDE_NAME]].to_numpy()
    
def get_y(data):
    if WORK_ITEM_NAME not in data.columns:
        raise ValueError("Check work item name")
    
    return data.loc[:, [WORK_ITEM_NAME]].to_numpy()
    
def get_y_new(newData):
    if WORK_ITEM_NAME_NEW not in newData.columns:
        raise ValueError("Check work item name")
    
    return newData.loc[:, [WORK_ITEM_NAME_NEW]].to_numpy()

def get_workloads(data):
    if WORKLOAD_NAME not in data.columns:
        raise ValueError("Check workload name")
        
    return data.loc[:, [WORKLOAD_NAME]].to_numpy()

def get_resulting_workloads(classifications):
    translations = pd.DataFrame({WORKLOAD_NAME: get_workloads(), WORK_ITEM_NAME: get_y()})
    
    def check_item(item):
        if item not in translations.loc[:, [WORK_ITEM_NAME]]:
            raise ValueError("Predicted work item not found in the workloads")
    [check_item(item) for item in classifications]
    
    classSeries = pd.Series({"classifications": classifications})
    workitems = pd.Series({WORK_ITEM_NAME: get_y_new()})
    workloadResults = classSeries.join(translations, how="left", on=["classifications", WORK_ITEM_NAME])
    workloadResults = workloadResults.loc[:, [WORKLOAD_NAME]
    results = pd.DataFrame([workloadResults, workitems])
    
    return results
    

def run_cleaner(data, newData):
    X = get_X()
    y = get_y()
    X_new = get_X_new(newData)
    workloads = get_workloads(data)
    
    return (X, y, X_new, workloads)
