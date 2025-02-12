import os

CLASSES = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

DATASET_PATH = "../dataset-resized"
OUTPUT_PATH = "../dados-yolo/labels"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# Percorrer as classes
for class_id, class_name in enumerate(CLASSES):
    class_path = os.path.join(DATASET_PATH, class_name)
    
    if not os.path.isdir(class_path):
        continue

    for file_name in os.listdir(class_path):
        if file_name.endswith(".jpg"):
            label_file = os.path.join(OUTPUT_PATH, file_name.replace(".jpg", ".txt"))
            
            with open(label_file, "w") as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")  