# TEAM_1114_STAS_II
## Competetion Reference
https://tbrain.trendmicro.com.tw/Competitions/Details/22

## Environments Building
1. 下載競賽連結中的 `SEG_Train_Datasets.zip` 並解壓縮，將裡面的 `Train_Annotations` 及 `Train_Images` 改名為 `All_Annotations` 及 `All_Images`
2. 執行 `preprocess.py` 以取出全部圖片的遮罩並儲存於 `All_Mask` 與 `All_Masked_Images` 中
3. 將 `All_Images` 及 `All_Mask` 中的 `00000800.jpg` ~ `00000919.jpg` 按下方格式放置於 `Valid` 資料夾，其餘則按相同格式放置於 `Train` 資料夾
4. 下載競賽連結中的 `Public_Image.zip` 及 `Private_Image.zip` ，解壓縮後放置於 `Inference_Images` 中
5. 執行 `get_model.sh` 下載比賽Ensemble使用的6個模型權重放置於 `Models` 中
6. `pip install requirements.txt` 以安裝使用到的套件
7. 接著即可按照 `STAS.ipynb` 中的操作訓練及驗證模型 (Ensemble於最下方)
8. 最終執行 `postprocess.py` 對預測結果進行後處理即可得到比賽上傳的最終成績

## Data Path
```
.
└── STAS
    ├── All_Annotations
    │   └── 00000000.json ~ 00001052.json
    ├── All_Images
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── All_Mask (Run 'preprocess.py' to generate, contain all groundtruth mask)
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── All_Masked_Images (Run 'preprocess.py' to generate, contain all groundtruth masked images)
    │   └── 00000000.jpg ~ 00001052.jpg
    ├── Inference_Images (Public & Private images to inference Leaderboard score)
    │   └── Private_00000000.jpg ~ Private_00000183.jpg & Public_00000000.jpg ~ Public_00000130.jpg
    ├── Models(Run 'get_model.sh' to download models' weight)
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
    ├── requirements.txt (For install toolkits)
    │
    └── STAS.ipynb (for training & inference model)
```
