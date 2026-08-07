from ultralytics import RTDETR

# 1. Load RT-DETR (Real-Time Transformer)
model = RTDETR('rtdetr-l.pt') 

# 2. Train with the exact same setup
results = model.train(
    data='./wet floor.yolo26/data.yaml',
    epochs=50,       
    imgsz=640,       
    batch=16, 
    name='wet_floor_rtdetr'
)

print("Training complete! Model saved in the 'runs/detect/wet_floor_rtdetr/weights/best.pt' folder.")