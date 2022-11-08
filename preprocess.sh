# bash copy_files.sh from 
# from : /mnt/c/Users/shung/Downloads

DATA_DIR=./SEG_Datasets
INFERENCE_DIR=$DATA_DIR/Inference_Images
ALL_IMAGES=$DATA_DIR/All_Images
ALL_ANNOTATIONS=$DATA_DIR/All_Annotations
ALL_MASK=$DATA_DIR/All_Mask
TRAIN=$DATA_DIR/Train
VALID=$DATA_DIR/Valid

# copy files
rsync -avPSH $1/SEG_Train_datasets.zip ./SEG_Train_datasets.zip
rsync -avPSH $1/Private_Image.zip ./Private_Image.zip
rsync -avPSH $1/Public_Image.zip ./Public_Image.zip

# zip files
unzip '*.zip'
rm *.zip

# rename
mv ./SEG_Train_Datasets/ $DATA_DIR
# inference folder
mkdir -p $INFERENCE_DIR
# rename Train_Annotations and Train_Images
mv $DATA_DIR/Train_Annotations $ALL_ANNOTATIONS
mv $DATA_DIR/Train_Images $ALL_IMAGES

# move Public_Image to $DATA_DIR folder
mv ./Public_Image/*.jpg $INFERENCE_DIR
# move Image to $DATA_DIR folder
mv ./Image/*.jpg $INFERENCE_DIR
# clean unused folder
rm -r ./Public_Image
rm -r ./Image

# preprocess SEG_Dataset to get Masked Images
python preprocess.py

# Train Valid Split 
mkdir -p $TRAIN/img # (00000000.jpg ~ 00000799.jpg + 00000920.jpg ~ 00001052.jpg)
cp -r $ALL_IMAGES/* $TRAIN/img

mkdir -p $TRAIN/label # (00000000.jpg ~ 00000799.jpg + 00000920.jpg ~ 00001052.jpg)
cp -r $ALL_MASK/* $TRAIN/label

mkdir -p $VALID/label # (00000800.jpg ~ 00000919.jpg)
find . -type f -ipath "$TRAIN/label/000008*.jpg" -exec mv {} $VALID/label  \;
find . -type f -ipath "$TRAIN/label/0000090*.jpg" -exec mv {} $VALID/label  \;
find . -type f -ipath "$TRAIN/label/0000091*.jpg" -exec mv {} $VALID/label  \;

mkdir -p $VALID/img # (00000800.jpg ~ 00000919.jpg)
find . -type f -ipath "$TRAIN/img/000008*.jpg" -exec mv {} $VALID/img  \;
find . -type f -ipath "$TRAIN/img/0000090*.jpg" -exec mv {} $VALID/img  \;
find . -type f -ipath "$TRAIN/img/0000091*.jpg" -exec mv {} $VALID/img  \;

echo DONE.