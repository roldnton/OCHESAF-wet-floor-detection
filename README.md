# Occupational Hazard Detection: Real-Time Wet Floor Monitoring
YOLO26, YOLO11, and RT-DETR-L AI models trained under the Wet Floor Dataset by TestDemo to detect wet spots on the floor for Occupational Health and Safety assistance. This repository contains the code and models for an automated computer vision safety system designed to detect wet floor hazards in real-time. This project evaluates and compares multiple state-of-the-art AI architectures for edge deployment.

## Repository Structure
*   **`Wet floor.yolo26/`** — The dataset directory containing the training images, validation images, and the `data.yaml` configuration file.
*   **`runs/`** — Automatically generated directory by Ultralytics containing model performance metrics (Precision, Recall, mAP, confusion matrices) and saved weights from training sessions.
*   **`yolo26.py`** — Training script for the end-to-end NMS-free YOLO26 Nano model.
*   **`yolo11.py`** — Training script for the YOLO11 Nano model.
*   **`rtdetr.py`** — Training script for the RT-DETR (Real-Time Detection Transformer) model.
*   **`realtime.py`** — The live-inference dashboard. This script hooks into a webcam (or video file), runs the chosen trained model, and outputs visual bounding boxes and hazard alerts in real-time.

# How to Use:
## Install Dependencies
`pip install ultralytics opencv-python`
## Train the Models
To train the models, run these files individually, where the results and best weights will be saved into the `runs/detect` folder:
`python yolo26.py
python yolo11.py
python rtdetr.py`
## Live Webcam Inference
After training the models, the live detection can be run in the file `realtime.py` in which the first section of the code allows you to choose between the three models trained, being configured with the "#" comment function. Press `q` to quit the live camera feed.

## Model Comparison and Results

_(still has to be filled up)_
| Model | Architecture | Parameters | Precision | Recall | mAP50
| -------- | -------- | -------- | -------- | -------- | -------- |
| YOLO26  | CNN  | ~ | ~ | ~ | ~ | 
| YOLO11  | CNN  | ~ | ~ | ~ | ~ | 
| RT-DETR Large | Vision Transformer | ~ | ~ | ~ | ~ | 

## Acknowledgements & Dataset Citation
This project utilizes the **Wet Floor Dataset** provided by user `TestDemo` on Roboflow Universe under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

```bibtex
@misc{ wet-floor-ecyia_dataset,
    title = { Wet floor Dataset },
    type = { Open Source Dataset },
    author = { TestDemo },
    howpublished = { \url{ [https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia](https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia) } },
    url = { [https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia](https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia) },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2025 },
    month = { oct },
}
