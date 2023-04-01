import os
import glob
import json
import subprocess
import shutil

def increment_values(data, x_increment, y_increment):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "x" or key == "X" \
                    or key == "TopLeftX" or key == "TopRightX"\
                    or key == "BottomLeftX" or key == "BottomRightX":
                data[key] = value + x_increment
            elif key == "y" or key == "Y" \
                    or key == "TopLeftY" or key == "TopRightY" \
                    or key == "BottomLeftY" or key == "BottomRightY":
                data[key] = value + y_increment
            else:
                if key != "Shape":
                    increment_values(value, x_increment, y_increment)
    elif isinstance(data, list):
        for item in data:
            increment_values(item, x_increment, y_increment)

# Get all JSON files in the current directory
bin_files = glob.glob("*.bin")

# Loop through all JSON files and remove them
for bin_file in bin_files:
    try:
        # run a command with arguments
        output = subprocess.check_output(['./MiBandWFTool_2.1.6/WatchFace.exe', bin_file])
        print(output)

        watch_name = os.path.splitext(bin_file)[0]

        json_filename = f"{watch_name}/{watch_name}.json"

        with open(json_filename) as f:
            data = json.load(f)

        # Increment values recursively
        increment_values(data, 13, 96)

        # Write modified JSON back to file
        with open(json_filename, "w") as f:
            json.dump(data, f)


        os.remove(f"{watch_name}/{watch_name}_animated.gif")
        os.remove(f"{watch_name}/{watch_name}_preview.png")
        os.remove(f"{watch_name}/{watch_name}_static.png")

        output = subprocess.check_output(['./MiBandWFTool_4.1.0/WatchFace.exe', json_filename])
        print(output)

        shutil.copy(f"{watch_name}/{watch_name}_packed.bin",
                    f"./all_bins/")

        os.remove(bin_file)
    except Exception:
        # code to handle the exception
        continue



