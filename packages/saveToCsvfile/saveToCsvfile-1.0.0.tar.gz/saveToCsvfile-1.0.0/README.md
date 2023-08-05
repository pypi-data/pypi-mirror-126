# saveToCsvfile
saveToCsvfile is a Python module that helps to save data into CSV file locally.  

## Basic Steps to use this module are as follows
1. Ensure that you have created "data.csv" in the directory of the file you use the module.
2. Ensure that you have installed the package successfully.
3. If the above two are completed, you are good to go to save the data locally into the backend.

### Now, you need to import the package using the following command
```
from saveToCsvfile import insertTo,fetchAll,fetch_N
```

## Above 3 functions, works as follows-
1. insertTo: Use this function in case you need to add data into CSV file. Remember, You need to add an array as a parameter and if this return 'Success'. You can paas n number of data, separated by commas into a single array. Check your "data.csv" file, data has been uploaded into the file. 
```
ins = insertTo(['One',2,3.0,True])
print(ins)
```

2. fetchAll: Use this function to fetch all the results present inside a file i.e "data.csv".
```
data = fetchAll()
print(data)
```

3. fetch_N: Use this function to fetch top N number of results present inside a file i.e "data.csv". Here, we need to paas a number as a parameter to fetch records. 
```
topTwo = fetch_N(2)
print(topTwo)
```
