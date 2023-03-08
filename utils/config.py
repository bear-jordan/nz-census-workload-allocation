from datetime import date

## Databases Headings
LONGITUDE_NAME = "Easting"
LATITUDE_NAME = "Northing"
WORK_ITEM_NAME = "Work Item ID"
WORKLOAD_NAME = "SF Workload ID"

## WCAT Headings
LONGITUDE_NAME_NEW = "Easting"
LATITUDE_NAME_NEW = "Northing"
WORK_ITEM_NAME_NEW = "Work Item ID"

## Filepaths
TEST_X_FILEPATH = ""
TEST_X_NEW_FILEPATH = ""
filepathHelper = "./results/"+date.today().strftime("%d-%m-%y")+"-"
RESULT_FILEPATH = filepathHelper + "new-workloads.csv"
