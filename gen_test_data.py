# Modules
import pandas as pd
import random

# Body
def gen_coordinate():
    return random.randint(-50, 50)

def check_workload(x, y):
    xi = "east" if x > 0 else "west"
    yi = "north" if y > 0 else "south"
    
    return yi + xi

def gen_data(n=10):
    x = [gen_coordinate() for i in range(n)]
    y = [gen_coordinate() for i in range(n)]
    wl = [check_workload(x[i], y[i]) for i in range(n)]

    return (x, y, wl)

def gen_wcat():
    x, y, _ = gen_data()
    data = pd.DataFrame({"latitude":y, "longitude":x, "workitem":list(range(10))})
    data.to_csv("./test-data/test-rand-wcat.csv", index=False)
    
    
def gen_current():
    x, y, wl = gen_data(25)
    data = pd.DataFrame({"latitude":y, "longitude":x, "workitem":list(range(11,36)), "workload":wl})
    data.to_csv("./test-data/test-rand-database.csv", index=False)
    
# gen_wcat()
# gen_current()