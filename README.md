# convert Mi Band5 to Mi Band6 watchface (python)

## Script Name: JSON Modification Tool

This is a Python function that takes in a JSON object, data, and two integer values,
x_increment and y_increment. The function recursively increments the values of the keys x, y, 
TopLeftX, TopRightX, BottomLeftX, BottomRightX, TopLeftY, TopRightY, BottomLeftY, 
BottomRightY by x_increment and y_increment respectively. 
The function also ignores the key Shape and loads the JSON object from a file named
black_neon_eco.json. The modified JSON object is then written back to the same file.


## Prerequisites:
- Python 3.6 or above
- MiBandWFTool


## Usage:
1. Copy .bin files to this folder.
2. Open the command prompt in the script directory.
3. Run the command `python.exe .\increment_json_by_values.py`. The script will perform the following tasks:
    * Extract data from the .bin file using the WatchFace.exe tool.
    * Modify the x and y values recursively in the extracted JSON data.
    * Repack the modified data back into a .bin file using the WatchFace.exe tool.


## Libraries Used:
- os
- glob
- json
- subprocess
- shutil


## Functionality:
1. The script extracts all .bin files from the current directory.
2. For each .bin file, the script uses the WatchFace.exe tool to extract the JSON data from the file.
3. The x and y values in the JSON data are incremented by specified values using the `increment_values()` function.
4. The modified JSON data is repacked into a .bin file using the WatchFace.exe tool.
5. The original .bin file is deleted, and the modified .bin file is moved to a specified directory.


## Note:
- The WatchFace.exe tool needs to be in the specified directories in the script.