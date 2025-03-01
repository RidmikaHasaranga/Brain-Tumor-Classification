import os
import shutil
import random

# Define dataset paths
train_dir = r"D:\IIT\Subjects\(4606)Machine Vision\CW\Develo\DataSet\Training"
test_dir = r"D:\IIT\Subjects\(4606)Machine Vision\CW\Develo\DataSet\Testing"
val_dir = r"D:\IIT\Subjects\(4606)Machine Vision\CW\Develo\DataSet\Validation"

# Class names in the dataset
classes = ['glioma', 'meningioma', 'notumor', 'pituitary']

# Validation split percentage
validation_split = 0.2  # 20% of training data

# Create validation directories
os.makedirs(val_dir, exist_ok=True)

for cls in classes:
    train_class_dir = os.path.join(train_dir, cls)
    val_class_dir = os.path.join(val_dir, cls)

    # Ensure the validation class directory exists
    os.makedirs(val_class_dir, exist_ok=True)

    # Get list of all images in the training class folder
    images = os.listdir(train_class_dir)
    
    # Shuffle and select validation split
    random.shuffle(images)
    val_count = int(len(images) * validation_split)
    val_images = images[:val_count]

    # Move selected images to validation folder
    for img in val_images:
        src_path = os.path.join(train_class_dir, img)
        dest_path = os.path.join(val_class_dir, img)
        shutil.move(src_path, dest_path)

    print(f"Moved {val_count} images from {cls} to validation dataset.")

print("Validation dataset created successfully.")
