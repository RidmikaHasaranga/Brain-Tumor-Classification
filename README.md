# 🧠 Brain Tumor Classification Using Deep Learning

This project implements and compares two deep learning approaches for the classification of brain tumors (Glioma, Meningioma, Pituitary) using MRI scans. It includes both segmentation and classification models, with a working prototype pipeline for testing a single image using saved models.

---

## 📁 Dataset

- Source: [Figshare Brain Tumor Dataset](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427)
- Tumor Types:
  - Glioma (1426 images)
  - Meningioma (708 images)
  - Pituitary (930 images)
- Data includes `.mat` MRI files and tumor segmentation masks.

---

## 📌 Methods

### ✅ Method 1: U-Net + Classification
1. **U-Net** segments the tumor from the MRI scan.
2. Tumor region is **cropped** using the segmentation mask.
3. Cropped image is classified using **EfficientNet**.

### ✅ Method 2: Whole Image Classification
- The entire MRI scan is directly classified using **EfficientNet** without segmentation.

---

## 📈 Results

| Metric                  | Method 1 (Segment + Classify) | Method 2 (Direct Classify) |
|-------------------------|-------------------------------|----------------------------|
| Test Accuracy           | 93.01%                        | 91.3%                      |
| Segmentation Accuracy   | 99.27% (U-Net)                | –                          |
| Dice Coefficient        | 0.6848                        | –                          |
| Precision / Recall (avg)| ~0.93                         | ~0.91                      |

---

## 🚀 How to Run the Prototype

> 💡 Run the notebook: `Brain_Tumor_Prototype_Pipeline.ipynb`

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/brain-tumor-classification.git
cd brain-tumor-classification

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the prototype pipeline
jupyter notebook Brain_Tumor_Prototype_Pipeline.ipynb


