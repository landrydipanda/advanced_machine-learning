# Face mask detection
As part of the fight against Covid-19, the main goal of this project is to create a machine learning model for the detection of masks on faces.

## Framework used
We used "yolov5".
Link to github: https://github.com/ultralytics/yolov5
Tutorial link: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
The dataset is contained in the TRAIN/ and TRAIN_2/ folders

## Preprocessing
Using Yolov5 requires special preprocessing
  - Modification of the configuration file: "masque_detection.yaml"
    -- specification of the training folder: train:/
    -- validation folder specification (853 Kaggles images): val:/
  - specification of the number of classes (with mask, without_mask, mask_weared_incorrect": nc: 3
  - Editing annotation files

YoloV5 uses .txt files for image annotation (confer tutorial)
We used the "convert_yolo_format.py" script for converting pascal voc xml annotations -> yolov5 .txt

## Training
Fixed parameters:
  - evolving learning rate during training
lr: 0.01
lrf:0.2
  - mosaic data increase
mosaic: 1.0

## Results
  - result_train_1: 15 epochs, batch of 16
  mAP: 0.798
    -- without_mask: 0.793
    -- with_mask: 0.936
    -- mask_weared_incorrect: 0.659
  - result_train_2: increase in the number of epochs (15 -> 35) and the batch size (16 -> 25) -> increase in mAP
  mAP: 0.802
    -- without_mask: 0.782
    -- with_mask: 0.930
    -- mask_weared_incorrect: 0.695
  - result_train_3: Test with TTA (test time increase) - > increase in mAP
For more information on the "TTA" optimizer: https://github.com/ultralytics/yolov5/issues/303
  mAP: 0.808
    without_mask: 0.791
    with_mask: 0.923
    mask_weared_incorrect: 0.802
