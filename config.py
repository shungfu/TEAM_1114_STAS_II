import os

DATA_ROOT = "SEG_Datasets"
MODEL_DIR = "./Models"

ALL_ANNOTATIONS_DIR = os.path.join(DATA_ROOT, "All_Annotations")
ALL_IMAGES_DIR =  os.path.join(DATA_ROOT, "All_Images")
ALL_MASK_DIR =  os.path.join(DATA_ROOT, "All_Mask")
ALL_MASK_IMAGES_DIR =  os.path.join(DATA_ROOT, "All_Masked_Images")

TRAIN_DIR = os.path.join(DATA_ROOT, "Train")
VALID_DIR = os.path.join(DATA_ROOT, "Train")

INFERENCE_IMAGE_DIR = os.path.join(DATA_ROOT, "Inference_Images")

ENSEMBLE_RST_DIR = "./Result/Result_Ensemble6_th043/"
ENSEMBLE_PRED_DIR = "./Result/Predictions_Ensemble6_th043/"
ENSEMBLE_MASK_DIR = "./Result/Masked_Result_Ensemble6_th043/"

SINGLE_PRED_DIR = "./Result/Predictions_Single_th043"