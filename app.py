import gradio as gr 
import cv2
import numpy as np 
from collections import Counter 
from ultralytics import YOLO  # Make sure you have this library installed

# Load the YOLOv10 model
model = YOLO("best.pt")

def predict(image):
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform prediction
    results = model.predict(source=image_rgb, imgsz=640, conf=0.25)
    
    # Get the annotated image
    annotated_img = results[0].plot()
    
    # Extract detection data
    detections = results[0].boxes.data
    class_names = [model.names[int(cls)] for cls in detections[:, 5]]
    count = Counter(class_names)

    # Create a string representation of the detections
    detection_str = ', '.join([f"{name}: {count}" for name, count in count.items()])

    return annotated_img, detection_str 

app = gr.Interface(
    predict, 
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=[gr.Image(type="numpy", label="Annotated Image"), gr.Textbox(label="Detection Counts")],
    title="Blood Cell Count", 
    description="Upload an image and YOLOv10 will detect blood cells"
)

app.launch()
