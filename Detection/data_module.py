import os
dictionary = {}

class_labels = ["person", "bicycle", "car", "motorbike", "aeroplane",  "bench", "bird", "cat", "dog", "backpack", "handbag",  "laptop", "mouse", "remote", "keyboard",
                    "cell phone", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
                    "scissors", "teddy bear", "hair drier", "toothbrush"]

directory_path = "/static/objects/"

# Construct file paths for each label
for label in class_labels:
    filepath = os.path.join(directory_path, label + ".jpg")
    dictionary[label] = filepath

