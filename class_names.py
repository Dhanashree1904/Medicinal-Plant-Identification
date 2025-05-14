import os
import json

# Path to your training data directory
train_data_dir = "C:/Users/admin/MYPROJECTS/MedicinalPlants/images"  # <-- Change this

# Get sorted list of class folder names
class_names = sorted(os.listdir(train_data_dir))

# Save to class_names.json
with open("class_names.json", "w") as f:
    json.dump(class_names, f)

print("class_names.json has been created with", len(class_names), "classes.")
