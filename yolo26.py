from ultralytics import YOLO

# 1. Load the YOLO26
model = YOLO('yolo26n.pt') 

# 2. Train the model on the local YAML file
results = model.train(
    data='./wet floor.yolo26/data.yaml', # Path to your YAML file
    epochs=50,       
    imgsz=640,       
    batch=16, 
    name='wet_floor_yolo26'
)

print("Training complete! Your model is saved in the 'runs/detect/wet_floor_yolo26/weights/best.pt' folder.")