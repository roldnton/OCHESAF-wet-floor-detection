from ultralytics import YOLO

# 1. Load the YOLO11
model = YOLO('yolo11n.pt') 

# 2. Train the model on the exact same dataset config
results = model.train(
    data='./wet floor.yolo26/data.yaml', # Path to your local YAML file
    epochs=50,       
    imgsz=640,       
    batch=16, 
    name='wet_floor_yolo11'
)

print("Training complete! Your model is saved in the 'runs/detect/wet_floor_yolo11/weights/best.pt' folder.")