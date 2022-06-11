# TEAM_1114_STAS_II
## Competetion Reference
https://tbrain.trendmicro.com.tw/Competitions/Details/22

## Data Path
```
.
└── STAS
    ├── All_Annotations
    │   └── 00000000.json ~ 00001052.json
    ├── All_Images
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── All_Mask (Run `preprocess.py` to generate, contain all groundtruth mask)
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── All_Masked_Images (Run `preprocess.py` to generate, contain all groundtruth masked images)
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── Inference_Images (Public & Private images to inference Leaderboard score)
    │   └── Private_00000000.jpg ~ Private_00000183.jpg & Public_00000000.jpg ~ Public_00000130.jpg
    ├── Models(Run `get_model.sh` to download models' weight)
    │   └── *.pth (total 6 models to ensemble)
    ├── Train (For model training, total 932 image)
    │   ├── img
    │   │   └── 00000000.jpg ~ 00000799.jpg + 00000920.jpg ~ 00001052.jpg
    │   └── label
    │       └── 00000000.jpg ~ 00000799.jpg + 00000920.jpg ~ 00001052.jpg
    ├── Valid (For model validation, total 120 image)
    │   ├── img
    │   │   └── 00000800.jpg ~ 00000919.jpg
    │   └── label
    │       └── 00000800.jpg ~ 00000919.jpg
    ├── get_model.sh (For downloading models' weight)
    │   
    ├── preprocess.py (For changing points to mask)
    │
    ├── postprocess.py (For postprocessing prediction to final result)
    │
    └── **STAS.ipynb** (for training & inference model)
```
