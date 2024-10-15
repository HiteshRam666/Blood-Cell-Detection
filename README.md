# 🩸 Blood Cell Detection & Counts 

Welcome to the **Blood Cell Counts** application! 🚀 This app is built to detect and classify blood cells using **YOLO (You Only Look Once)** object detection and provides an intuitive interface powered by **Gradio**. 🧬🔬

App Link 👉: https://huggingface.co/spaces/HiteshRam/Blood_Cell_Detection

## 🌟 Project Overview

This project aims to simplify the process of **blood cell image analysis** using the **YOLO** object detection algorithm. YOLO is employed to identify and count different types of blood cells, such as **Red Blood Cells (RBCs)**, **White Blood Cells (WBCs)**, and **Platelets**, in microscopic images. The goal is to create a fast, automated solution that reduces the time and effort required for manual cell counting and classification. With the help of **Gradio**, we provide a web-based interface for users to upload images, run detections, and receive real-time results.

## 🔑 Key Components

- **YOLO Object Detection**: Detect and classify different types of blood cells in images using the YOLO model.
- **Gradio Interface**: An easy-to-use web interface for image upload and result display.
- **Real-time Predictions**: Quickly analyze images and view bounding boxes around detected blood cells.

## 📊 Why This Project is Important

Manual blood cell counting can be time-consuming and prone to human error, especially when processing large amounts of data. This project leverages AI to provide:
- **Faster detection and classification** of blood cells.
- **Real-time results**, helping to save time and effort.
- **Accurate and consistent** cell counts, which are critical in diagnosing blood-related diseases such as anemia, leukemia, and other conditions.

## ⚙️ How It Works

### 1. Upload Blood Cell Image
Users can upload an image of a blood sample through the Gradio interface.

### 2. YOLO Model Processes the Image
The **YOLO** object detection model processes the image and identifies:
- **Red Blood Cells (RBCs)**
- **White Blood Cells (WBCs)**
- **Platelets**

Bounding boxes are drawn around each detected blood cell, and the model also classifies each cell type.

### 3. Real-Time Detection Results
- Bounding boxes around blood cells with **class labels**.
- **Counts** for each type of blood cell in the image.
- Real-time, visual output for easy inspection.

## 🖼️ Sample Output

![download (19)](https://github.com/user-attachments/assets/9fad3321-99a7-448a-95c9-e14484918688)
![download (20)](https://github.com/user-attachments/assets/21311939-1407-40d2-8ed2-cb5475d8eae7)


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/blood-cell-counts.git
cd blood-cell-counts
```

### 2. Install Dependencies

Make sure to have Python installed. Then, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 3. Run the App

Start the Gradio app by running the following command:

```bash
python app.py
```

Gradio will automatically launch the app in your browser. If not, you can manually open the URL shown in the terminal.

## 🛠️ Technologies Used

- **YOLO** - For fast, real-time object detection.
- **Gradio** - For creating an easy-to-use web interface.
- **Python** - Backend logic and processing.
- **Machine Learning** - Model trained to detect and classify blood cells.

## 🤖 YOLO Model

YOLO, short for **You Only Look Once**, is one of the fastest and most accurate object detection algorithms. It divides the image into a grid, predicts bounding boxes for objects, and assigns class labels to each detected object. In this project, YOLO is trained to detect small objects, such as blood cells, and classify them accurately.

### Why YOLO?

- **Speed**: YOLO processes the entire image in a single forward pass, making it one of the fastest detection models available.
- **Accuracy**: The model's ability to detect small objects like platelets makes it ideal for this application.

## 🌍 Use Cases

- **Medical Diagnostics**: Assisting doctors and pathologists in analyzing blood samples.
- **Medical Research**: Helping researchers process large datasets of blood images efficiently.
- **Education**: Demonstrating the power of AI in medical image analysis for students and educators.

## 🛠️ Future Scope

- **Improving the Model**: Training on larger datasets with more diverse blood cell types to increase detection accuracy.
- **Expanding Cell Subtypes**: Extending the model to detect subtypes of white blood cells, such as lymphocytes and monocytes.
- **Integration with Diagnostic Tools**: Real-time analysis integration with microscopes for immediate results during blood tests.

## 🤝 Contributing

We welcome contributions from the community! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Push to the branch.
5. Create a pull request.
