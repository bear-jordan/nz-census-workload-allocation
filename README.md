# nz-census-workload-allocation
KNN implementation for workload allocation

1. Clone the directory and navigate to the root folder.
2. Download the new WCAT run and download the current work items report. See the reports with the following titles: Unallocated Work Items from WCAT, and 09/03/23 WCAT run created Workloa
3. Rename them something simple (e.g., "wcat.csv" and "db.csv"). 
4. Place the files into the `.\data\` folder.
5. `pip install -r requirements.txt`
6. `python main.py PATH_TO_WCAT PATH_TO_DB`
7. Check out the `.\results\` folder. The new assignments are outputted with the current date.
