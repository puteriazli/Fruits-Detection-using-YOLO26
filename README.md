::: {align="center"}
# 🍎 Fruits Image Detection

**Object Detection & Classification of Fruits using YOLO26n**

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/Ultralytics-YOLO-111111?style=flat-square" alt="Ultralytics YOLO">`{=html}
`<img src="https://img.shields.io/badge/mAP50-89.6%25-success?style=flat-square" alt="mAP50">`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

## Overview

**Fruits Image Detection** adalah project **computer vision** berbasis
Artificial Intelligence untuk mendeteksi dan mengklasifikasikan objek
buah pada gambar menggunakan **YOLO26n** dan Python.

Project mencakup seluruh alur mulai dari **dataset preparation,
auto-labeling, quality control, model training, validation, penyimpanan
model**, hingga **inference menggunakan gambar lokal**.

## ✨ Fitur Utama

-   Download dataset langsung dari Kaggle menggunakan `kagglehub`
-   Automatic dataset discovery dan pembacaan `data.yaml`
-   Preparation dataset ke format YOLO
-   Auto-labeling menggunakan `yolov8s-worldv2.pt`
-   Pemanfaatan `_classes.csv` sebagai informasi class ground-truth
-   Fallback bounding box apabila objek tidak berhasil dideteksi oleh
    labeler
-   Quick Quality Control (QC) dengan visualisasi bounding box
-   Training menggunakan **YOLO26n**
-   Evaluasi menggunakan **Precision, Recall, mAP50, dan mAP50-95**
-   Penyimpanan bobot model terbaik
-   Export model ke Google Drive
-   Inference lokal menggunakan `inference.py`

## 📊 Project at a Glance

  Komponen               Detail
  ---------------------- -----------------------------------
  Task                   Object Detection
  Model                  YOLO26n
  Auto-labeler           YOLOv8s-WorldV2
  Dataset                Fruits by YOLO - Fruits Detection
  Number of Classes      9
  Image Size             640 × 640
  Epochs                 25
  Batch Size             16
  Validation mAP50       **89.6%**
  Validation mAP50-95    **83.5%**
  Training Environment   Google Colab
  Local Inference        Python + OpenCV

> **Catatan:** Metric di atas berasal dari hasil validation run yang
> tersedia pada project. Karena sebagian label dibuat melalui
> **auto-labeling**, hasil evaluasi perlu dipahami sebagai evaluasi
> terhadap dataset/label yang telah dipersiapkan secara otomatis.

------------------------------------------------------------------------

## 🗂️ Dataset

Dataset yang digunakan:

**Fruits by YOLO - Fruits Detection**

Sumber:

https://www.kaggle.com/datasets/kapturovalexander/fruits-by-yolo-fruits-detection

Dataset diakses melalui:

``` python
DATASET_HANDLE = "kapturovalexander/fruits-by-yolo-fruits-detection"
```

Dataset memiliki tiga split utama:

``` text
train
valid
test
```

Nama class dibaca dari `data.yaml`. Project juga menyediakan fallback
class names apabila `data.yaml` tidak dapat dibaca.

### Class yang digunakan

    \# Class
  ---- ------------
     1 Apple
     2 Banana
     3 Grapes
     4 Kiwi
     5 Mango
     6 Orange
     7 Pineapple
     8 Sugerapple
     9 Watermelon

------------------------------------------------------------------------

## 🛠️ Teknologi

  Komponen               Teknologi
  ---------------------- --------------------
  Programming Language   Python
  Object Detection       Ultralytics YOLO
  Training Model         YOLO26n
  Auto-labeling          YOLOv8s-WorldV2
  Computer Vision        OpenCV
  Deep Learning          PyTorch
  Dataset Download       KaggleHub
  Data Processing        Pandas
  YAML Processing        PyYAML
  Visualization          Matplotlib
  Environment            Anaconda
  IDE                    Visual Studio Code
  Training               Google Colab
  Storage                Google Drive
  Dataset Source         Kaggle

------------------------------------------------------------------------

## 💻 Spesifikasi Sistem Pengerjaan

  Spesifikasi            Detail
  ---------------------- ---------------------------------
  Device                 Lenovo IdeaPad Slim 14
  Operating System       Windows
  Processor              Intel Core i5 Generasi ke-11
  RAM                    16 GB
  Local GPU              Tidak menggunakan GPU dedicated
  Environment Manager    Anaconda
  Terminal               Anaconda Prompt
  Code Editor            Visual Studio Code
  Training Environment   Google Colab
  Model                  YOLO26n
  Image Size             640 × 640
  Epochs                 25
  Batch Size             16

> **Catatan:** Training dilakukan menggunakan Google Colab karena
> komputer lokal tidak menggunakan GPU dedicated. Model hasil training
> tetap dapat digunakan untuk inference pada komputer lokal.

------------------------------------------------------------------------

## 📁 Struktur Project

``` text
fruits-image-detection/
│
├── images/
│   └── 2.jpg
│
├── models/
│   └── yolo26n_models.pt
│
├── notebooks/
│   └── fruit_image_detection.ipynb
│
├── inference.py
├── LICENSE
├── requirements.txt
└── tutorial.txt
```

### Penjelasan

**`images/`**\
Berisi gambar yang digunakan sebagai input inference.

**`models/`**\
Berisi model hasil training. Model utama:

``` text
yolo26n_models.pt
```

**`notebooks/`**\
Berisi notebook Google Colab untuk dataset preparation, auto-labeling,
QC, training, validation, dan export model.

**`inference.py`**\
Script untuk menjalankan object detection pada komputer lokal.

**`requirements.txt`**\
Daftar package Python yang diperlukan untuk menjalankan project.

**`tutorial.txt`**\
Berisi panduan tambahan penggunaan project.

------------------------------------------------------------------------

## 🔄 Project Pipeline

``` text
Kaggle Dataset
      ↓
Download via KaggleHub
      ↓
Dataset Discovery
      ↓
Read data.yaml + _classes.csv
      ↓
Dataset Preparation
      ↓
Auto-labeling
      ↓
Quality Control
      ↓
YOLO Dataset
      ↓
YOLO26n Training
      ↓
Model Validation
      ↓
best.pt
      ↓
Export to Google Drive
      ↓
Local Inference
      ↓
Annotated Detection Image
```

------------------------------------------------------------------------

## ⚙️ Instalasi

### 1. Buat Environment Anaconda

Buka **Anaconda Prompt**:

``` bash
conda create -n fruits_detection python
```

Aktifkan environment:

``` bash
conda activate fruits_detection
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

Verifikasi Ultralytics:

``` bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

Verifikasi OpenCV:

``` bash
python -c "import cv2; print(cv2.__version__)"
```

------------------------------------------------------------------------

## ☁️ Training di Google Colab

Notebook menggunakan Google Colab untuk proses training.

Library utama:

``` python
!pip install -q -U ultralytics kagglehub pyyaml pandas
```

Dataset diunduh menggunakan:

``` python
import kagglehub

DATASET_HANDLE = "kapturovalexander/fruits-by-yolo-fruits-detection"

cache_path = kagglehub.dataset_download(DATASET_HANDLE)
```

### Training Configuration

``` python
BASE_MODEL = "yolo26n.pt"

EPOCHS = 25
IMG_SIZE = 640
BATCH_SIZE = 16
```

Training dilakukan dengan:

``` python
model.train(
    data=str(NEW_DATA_YAML),
    epochs=EPOCHS,
    imgsz=IMG_SIZE,
    batch=BATCH_SIZE,
    project=PROJECT_DIR,
    name=RUN_NAME,
    patience=15,
    verbose=True,
)
```

------------------------------------------------------------------------

## 🏷️ Auto-Labeling

Auto-labeling menggunakan:

``` python
LABELER_MODEL = "yolov8s-worldv2.pt"
```

Model digunakan untuk menghasilkan bounding box objek buah dalam format
YOLO.

Konfigurasi:

``` python
CONF_THRESHOLD = 0.20
LABELER_IMGSZ = 480
BATCH_SIZE_LABELING = 4
```

Informasi class dari `_classes.csv` digunakan untuk membantu menentukan
class yang benar pada masing-masing gambar.

Jika sebuah class diketahui terdapat pada gambar tetapi tidak berhasil
ditemukan oleh labeler, project menggunakan **fallback full-image
bounding box**.

Konfigurasi device:

``` python
USE_GPU = torch.cuda.is_available()

QUANTIZE = 16 if USE_GPU else 32
```

------------------------------------------------------------------------

## 🧩 Dataset Format

Dataset hasil preparation memiliki struktur:

``` text
data_prepared/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

`data.yaml` dibuat otomatis oleh notebook:

``` yaml
train: /content/data_prepared/train/images
val: /content/data_prepared/valid/images
test: /content/data_prepared/test/images

nc: <jumlah kelas>

names:
  - ...
```

------------------------------------------------------------------------

## 🔍 Quality Control

Notebook menyediakan fungsi `quick_qc()` untuk mengambil sample gambar
dan menampilkan bounding box hasil auto-labeling.

Contoh:

``` python
quick_qc("train", n=6)
```

QC dilakukan untuk memeriksa secara visual apakah bounding box hasil
auto-labeling sudah berada pada objek yang sesuai sebelum proses
training.

------------------------------------------------------------------------

## 📈 Model Evaluation

Setelah training selesai, model divalidasi menggunakan:

``` python
metrics = model.val()
```

Metric utama:

-   **Precision**
-   **Recall**
-   **mAP50**
-   **mAP50-95**

Hasil dapat ditampilkan dengan:

``` python
print("mAP50:", metrics.box.map50)
print("mAP50-95:", metrics.box.map)
```

### Validation Result

  Metric           Result
  ----------- -----------
  Precision     **89.3%**
  Recall        **84.1%**
  mAP50         **89.6%**
  mAP50-95      **83.5%**

### Per-Class Validation Result

  Class          Precision   Recall   mAP50   mAP50-95
  ------------ ----------- -------- ------- ----------
  Apple              88.2%    93.3%   94.9%      93.8%
  Banana             96.5%    77.4%   88.3%      75.8%
  Grapes             92.4%    75.8%   87.5%      73.1%
  Kiwi               94.3%   100.0%   95.6%      94.0%
  Mango             100.0%    91.7%   97.8%      95.4%
  Orange             69.4%    68.6%   72.9%      63.7%
  Pineapple          73.3%    71.0%   74.9%      64.1%
  Sugerapple         94.8%   100.0%   99.5%      99.5%
  Watermelon         94.6%    79.1%   94.9%      92.3%

**Validation dataset:** 187 images, 248 instances.

> **Evaluation note:** Angka di atas merupakan hasil **validation** dari
> run yang tersedia. Training metrics dan independent test metrics tidak
> dicantumkan sebagai angka karena tidak tersedia pada output evaluasi
> yang digunakan untuk dokumentasi ini.

------------------------------------------------------------------------

## 📦 Model

Bobot terbaik setelah training:

``` text
best.pt
```

Kemudian model disimpan dengan nama:

``` text
yolo26n_models.pt
```

### Google Drive

``` text
MyDrive/
└── Projek/
    └── Fruits Detection (Object Detection)/
        └── models/
            └── yolo26n_models.pt
```

Model kemudian digunakan oleh inference lokal melalui:

``` python
MODEL_PATH = "models/yolo26n_models.pt"
```

------------------------------------------------------------------------

## 🖼️ Inference

Inference dapat dijalankan secara lokal menggunakan:

``` text
inference.py
```

Pastikan struktur file:

``` text
models/
└── yolo26n_models.pt

images/
└── 2.jpg
```

Kemudian jalankan:

``` bash
python inference.py
```

Confidence threshold:

``` python
CONF_THRESHOLD = 0.4
```

Contoh konfigurasi:

``` python
MODEL_PATH = "models/yolo26n_models.pt"
IMAGE_PATH = "images/2.jpg"
CONF_THRESHOLD = 0.4

model = YOLO(MODEL_PATH)

result = model.predict(
    source=IMAGE_PATH,
    conf=CONF_THRESHOLD,
    verbose=False
)[0]

annotated_frame = result.plot()
```

Hasil detection akan ditampilkan pada window OpenCV.

Tekan tombol apa saja pada window gambar untuk menutup hasil inference.

------------------------------------------------------------------------

## ☁️ Google Drive Export

Notebook menggunakan Google Drive untuk menyimpan model hasil training:

``` python
from google.colab import drive

drive.mount('/content/drive')
```

Model disalin ke:

``` text
MyDrive/Projek/Fruits Detection (Object Detection)/models/yolo26n_models.pt
```

------------------------------------------------------------------------

## ⚠️ Keterbatasan

1.  Training dilakukan di Google Colab karena komputer lokal tidak
    menggunakan GPU dedicated.
2.  Waktu training dapat berbeda tergantung resource GPU Google Colab
    yang tersedia.
3.  Hasil auto-labeling bergantung pada kemampuan model
    `yolov8s-worldv2`.
4.  Fallback bounding box digunakan ketika class diketahui dari
    `_classes.csv`, tetapi objek tidak berhasil ditemukan oleh labeler.
5.  Metric dapat berbeda apabila proses training dijalankan kembali.
6.  Versi Python, PyTorch, CUDA, dan Ultralytics dapat memengaruhi
    kompatibilitas serta performa.
7.  Karena sebagian label diperoleh melalui proses auto-labeling, hasil
    validation tidak dapat dianggap sebagai evaluasi terhadap
    ground-truth manual yang sepenuhnya independen.

------------------------------------------------------------------------

## 👤 Credits

**Puteri Amelia Azli**

Project / notebook dibuat pada:

**16 September 2026**

### Portfolio

-   GitHub: https://github.com/puteriazli
-   LinkedIn: https://www.linkedin.com/in/puteriazli
-   Kaggle: https://www.kaggle.com/puteriameliaazli
-   YouTube: https://www.youtube.com/@putericoding

------------------------------------------------------------------------

## 📄 License

Project ini menyertakan file `LICENSE`.

Silakan merujuk langsung ke file tersebut untuk ketentuan penggunaan,
distribusi, dan modifikasi project.

------------------------------------------------------------------------

::: {align="center"}
**Fruits Image Detection · YOLO26n · Python**
:::
