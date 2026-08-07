# A Comparative Analysis of YOLO and RT-DETR in Occupational Hazard Detection of Wet Floors
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
* `python yolo26.py`
* `python yolo11.py`
* `python rtdetr.py`
## Live Webcam Inference
After training the models, the live detection can be run in the file `realtime.py`, in which the first section of the code allows you to choose between the three models trained, configured with the `#` comment function. Press `q` to quit the live camera feed.

# Model Comparison and Results
The models are compared with each other using these metrics:
__`Precision`__: How often they are right in identifying wet floors
**`Recall`**: How often they miss the hazard
**`mAP50`**: Overall detection score
**`mAP50-95`**: Box quality and accuracy

After running 50 epochs for training the AI, here are the results from the last run:
| Model | Architecture | Precision | Recall | mAP50 | mAP50-95 |
| -------- | -------- | -------- | -------- | -------- | -------- |
| YOLO26  | CNN  | 0.63205 | 0.25 | 0.30223 | 0.30223 | 0.11987 |
| YOLO11  | CNN  | 0.39156 | 0.50055 | 0.38486 | 0.17236 |
| RT-DETR Large | Vision Transformer | 0.47209 | 0.36111 | 0.31375 | 0.15323 |

**YOLO26** shows values that indicate it achieves the highest precision by a wide margin, providing a 63.2% percentage, with its biggest drawback being its low recall value, 25%.

**YOLO11** shows the highest overall detection score as its mAP50 value is 38.4%, and the highest recall value of 50%. On the other hand, its precision score is a low 39.1%, meaning that more than half the time it alerts you of a wet floor, it was a false alarm.

**RT-DETR** shows values that prove that Transformers are too heavy for this particular task, as its precision value lies between the other two (47.2%) with a recall of 36.1%. The mAP50 value was also barely better than YOLO26, giving a percentage of 31.3%, not justifying the computational power this model uses compared to the two YOLO models.

The mAP50-95 values for all the models show extremely low scores, which tells us that even is the models find the wet floor, the boxes bounding it are very imprecise. This suggests that more training would benefit the models, as they were able to learn where the wet spots would roughly be, but they did not have enough time to figure out how to precisely draw the boxes around it.

## Acknowledgements, Dataset, Framework, and Model Citations
If you use this repository or build upon this research, please cite the underlying architectures as follows:

### YOLO26
```bibtex
@misc{jocher2026ultralyticsyolo26unifiedrealtime,
  title = {Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models},
  author = {Glenn Jocher and Jing Qiu and Mengyu Liu and Shuai Lyu and Fatih Cagatay Akyon and Muhammet Esat Kalfaoglu},
  year = {2026},
  eprint = {2606.03748},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  doi = {10.48550/arXiv.2606.03748},
  url = {https://arxiv.org/abs/2606.03748},
}
```

### YOLO11
```bibtex
@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

### RT-DETR
```bibtex
@misc{lv2023detrs,
      title={DETRs Beat YOLOs on Real-time Object Detection},
      author={Wenyu Lv and Shangliang Xu and Yian Zhao and Guanzhong Wang and Jinman Wei and Cheng Cui and Yuning Du and Qingqing Dang and Yi Liu},
      year={2023},
      eprint={2304.08069},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

This project utilizes the **Wet Floor Dataset** provided by user `TestDemo` on Roboflow Universe under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

```bibtex
@misc{ wet-floor-ecyia_dataset,
  title = { Wet floor Dataset },
  type = { Open Source Dataset },
  author = { TestDemo },
  howpublished = { \url{ https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia } },
  url = { https://universe.roboflow.com/testdemo-orvjj/wet-floor-ecyia },
  journal = { Roboflow Universe },
  publisher = { Roboflow },
  year = { 2025 },
  month = { oct },
  note = { visited on 2026-08-07 },
}
```
