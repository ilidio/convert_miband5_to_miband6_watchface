import json

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

# Load JSON from file
json_filename = "black_neon_eco.json"

with open(json_filename) as f:
    data = json.load(f)

# Increment values recursively
increment_values(data, 13, 96)

# Write modified JSON back to file
with open(json_filename, "w") as f:
    json.dump(data, f)

