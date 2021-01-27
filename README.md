
# advanced_machine-learning
Projet ML Avancee / Détection d'objets : application à la detection de masques dans les images

#Framework utilisé
Nous avons utilisé "yolov5". 
Lien vers le github : https://github.com/ultralytics/yolov5
Lien vers le tutoriel : https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data
Le dataset est contenu dans le dossier TRAIN/ et TRAIN_2/

#Preprocessing 
L'utilisation de Yolov5 necessite un preprocessing particulier 
  #Modification du fichier de configuration : "masque_detection.yaml" 
  - specification du du dossier d'entrainnement : train:/
  - specification du dossier de validation ( 853 images de Kaggles ) : val:/ 
  - specification du nombre de classes (with mask, without_mask, mask_weared_incorrect" : nc : 3
  #Modification des fichiers d'annotations 
YoloV5 utilise les fichiers .txt pour l'annotation des images ( confère tutoriel)
Nous avons utilisé le script "convert_yolo_format.py" pour la conversion des annotations pascal voc xml ->  yolov5 .txt 

#Trainning 
Paramètres fixes :
  #learning rate evolutif pendant l'entrainnement 
lr: 0.01
lrf:0.2
  #mosaic data augmentation
mosaic : 1.0

/result_train_1 : 15 epochs, batch de 16
  #mAP : 0.798
    without_mask : 0.793
    with_mask : 0.936
    mask_weared_incorrect : 0.659
/result_train_2 : augmentation du nombre d'epochs ( 15 -> 35 ) et la taille de batch (16 -> 25) -> augmentation de mAP
  #mAP : 0.802
    without_mask : 0.782
    with_mask : 0.930
    mask_weared_incorrect : 0.695
/result_train_3 : Test avec TTA ( test time augmentation) - > augmentation de mAP
Pour plus d'information sur l'optimiseur "TTA" : https://github.com/ultralytics/yolov5/issues/303
  #mAP : 0.808
    without_mask : 0.791
    with_mask : 0.923
    mask_weared_incorrect : 0.802
