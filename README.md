# 🍎 Fruits Image Detection

**Object Detection & Classification of Fruits using YOLO26n**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO-111111?style=flat-square)
![mAP50](https://img.shields.io/badge/mAP50-89.6%25-success?style=flat-square)

---

## Overview

**Fruits Image Detection** adalah project **computer vision** berbasis Artificial Intelligence untuk mendeteksi dan mengklasifikasikan objek buah pada gambar menggunakan **YOLO26n** dan Python.

Project mencakup seluruh alur mulai dari **dataset preparation, auto-labeling, quality control, model training, validation, penyimpanan model**, hingga **inference menggunakan gambar lokal**.

## ✨ Fitur Utama

- Download dataset langsung dari Kaggle menggunakan `kagglehub`
- Automatic dataset discovery dan pembacaan `data.yaml`
- Preparation dataset ke format YOLO
- Auto-labeling menggunakan `yolov8s-worldv2.pt`
- Pemanfaatan `_classes.csv` sebagai informasi class ground-truth
- Fallback bounding box apabila objek tidak berhasil dideteksi oleh labeler
- Quick Quality Control (QC) dengan visualisasi bounding box
- Training menggunakan **YOLO26n**
- Evaluasi menggunakan **Precision, Recall, mAP50, dan mAP50-95**
- Penyimpanan bobot model terbaik
- Export model ke Google Drive
- Inference lokal menggunakan `inference.py`

---

## 📊 Project at a Glance

| Item | Detail |
|---|---|
| **Task** | Object Detection |
| **Model** | YOLO26n |
| **Auto-labeler** | YOLOv8s-WorldV2 |
| **Dataset** | Fruits by YOLO - Fruits Detection |
| **Classes** | 9 |
| **Image Size** | 640 × 640 |
| **Epochs** | 25 |
| **Batch Size** | 16 |
| **Validation mAP50** | **89.6%** |
| **Validation mAP50-95** | **83.5%** |
| **Training** | Google Colab |
| **Inference** | Python + OpenCV |

> **Catatan:** Metric di atas berasal dari hasil validation run yang tersedia pada project. Karena sebagian label dibuat melalui **auto-labeling**, hasil evaluasi perlu dipahami sebagai evaluasi terhadap dataset/label yang telah dipersiapkan secara otomatis.

---

## 🗂️ Dataset

**Dataset:** [Fruits by YOLO - Fruits Detection](https://www.kaggle.com/datasets/kapturovalexander/fruits-by-yolo-fruits-detection)

Dataset diakses melalui KaggleHub:

```python
DATASET_HANDLE = "kapturovalexander/fruits-by-yolo-fruits-detection"
```

### Dataset Split

| Split | Fungsi |
|---|---|
| `train` | Training model |
| `valid` | Validation model |
| `test` | Dataset untuk testing/inference evaluation |

Nama class dibaca dari `data.yaml`. Project juga menyediakan fallback class names apabila `data.yaml` tidak dapat dibaca.

### Class yang Digunakan

| # | Class |
|---:|---|
| 1 | Apple |
| 2 | Banana |
| 3 | Grapes |
| 4 | Kiwi |
| 5 | Mango |
| 6 | Orange |
| 7 | Pineapple |
| 8 | Sugerapple |
| 9 | Watermelon |

---

## 🛠️ Teknologi & Tools

| Kategori | Teknologi / Tools | Penggunaan |
|---|---|---|
| **Programming** | Python | Pengembangan project |
| **Object Detection** | Ultralytics YOLO | Training & inference |
| **Training Model** | YOLO26n | Model utama |
| **Auto-labeling** | YOLOv8s-WorldV2 | Pembuatan bounding box |
| **Computer Vision** | OpenCV | Image processing & inference |
| **Deep Learning** | PyTorch | Backend deep learning |
| **Data Processing** | Pandas | Pengolahan data |
| **YAML Processing** | PyYAML | Membaca & membuat `data.yaml` |
| **Visualization** | Matplotlib | Quality Control |
| **Dataset** | Kaggle + KaggleHub | Sumber & download dataset |
| **Environment** | Anaconda | Python environment |
| **IDE** | Visual Studio Code | Development |
| **Training Platform** | Google Colab | Model training |
| **Storage** | Google Drive | Penyimpanan model |

---

## 💻 Spesifikasi Sistem Pengerjaan

### Local Development

| Komponen | Spesifikasi |
|---|---|
| **Device** | Lenovo IdeaPad Slim 14 |
| **Operating System** | Windows 11 |
| **Processor** | Intel Core i5 Generasi ke-11 |
| **RAM** | 16 GB |
| **Local GPU** | Tidak menggunakan GPU dedicated |
| **Environment Manager** | Anaconda |
| **Terminal** | Anaconda Prompt |
| **Code Editor** | Visual Studio Code |

### Training Configuration

| Parameter | Value |
|---|---:|
| **Training Platform** | Google Colab |
| **Model** | YOLO26n |
| **Image Size** | 640 × 640 |
| **Epochs** | 25 |
| **Batch Size** | 16 |
| **Patience** | 15 |

> **Catatan:** Training dilakukan menggunakan Google Colab karena komputer lokal tidak menggunakan GPU dedicated. Model hasil training tetap dapat digunakan untuk inference pada komputer lokal.

---

## 📁 Struktur Project

```text
fruits-image-detection/
│
├── images/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   └── pisang.jpg
│
├── models/
│   └── yolo26n_models.pt
│
├── notebooks/
│   └── fruit_image_detection.ipynb
│
├── inference.py
├── LICENSE
└── requirements.txt
```

### File & Folder

| Path | Keterangan |
|---|---|
| `images/` | Gambar input untuk inference |
| `models/` | Menyimpan model hasil training |
| `notebooks/` | Notebook untuk dataset preparation, auto-labeling, QC, training, validation, dan export |
| `inference.py` | Script object detection lokal |
| `requirements.txt` | Dependencies Python project |
| `LICENSE` | File lisensi project |

---

## 🔄 Project Pipeline

```text
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

---

## ⚙️ Instalasi

### 1. Buat Environment Anaconda

Buka **Anaconda Prompt**:

```bash
conda create -n fruits_detection python
```

Aktifkan environment:

```bash
conda activate fruits_detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Verifikasi Instalasi

**Ultralytics:**

```bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

**OpenCV:**

```bash
python -c "import cv2; print(cv2.__version__)"
```

---

## ☁️ Training di Google Colab

Notebook menggunakan Google Colab untuk proses training.

### Install Library

```python
!pip install -q -U ultralytics kagglehub pyyaml pandas
```

### Download Dataset

```python
import kagglehub

DATASET_HANDLE = "kapturovalexander/fruits-by-yolo-fruits-detection"

cache_path = kagglehub.dataset_download(DATASET_HANDLE)
```

### Training Configuration

| Parameter | Value |
|---|---|
| **Base Model** | `yolo26n.pt` |
| **Epochs** | 25 |
| **Image Size** | 640 |
| **Batch Size** | 16 |
| **Patience** | 15 |

```python
BASE_MODEL = "yolo26n.pt"
EPOCHS = 25
IMG_SIZE = 640
BATCH_SIZE = 16
```

### Training

```python
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

---

## 🏷️ Auto-Labeling

Auto-labeling menggunakan:

```python
LABELER_MODEL = "yolov8s-worldv2.pt"
```

Model digunakan untuk menghasilkan bounding box objek buah dalam format YOLO.

### Konfigurasi Auto-Labeling

| Parameter | Value |
|---|---:|
| **Labeler Model** | `yolov8s-worldv2.pt` |
| **Confidence Threshold** | `0.20` |
| **Labeling Image Size** | `480` |
| **Labeling Batch Size** | `4` |

Informasi class dari `_classes.csv` digunakan untuk membantu menentukan class yang benar pada masing-masing gambar.

Jika sebuah class diketahui terdapat pada gambar tetapi tidak berhasil ditemukan oleh labeler, project menggunakan **fallback full-image bounding box**.

### Device Configuration

| Parameter | Value |
|---|---|
| **GPU Available** | `torch.cuda.is_available()` |
| **Quantization** | `16` jika GPU tersedia, `32` jika CPU |

```python
USE_GPU = torch.cuda.is_available()

QUANTIZE = 16 if USE_GPU else 32
```

---

## 🧩 Dataset Format

Dataset hasil preparation memiliki struktur:

```text
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

### `data.yaml`

| Parameter | Value |
|---|---|
| **train** | `/content/data_prepared/train/images` |
| **val** | `/content/data_prepared/valid/images` |
| **test** | `/content/data_prepared/test/images` |
| **nc** | `<jumlah kelas>` |
| **names** | Daftar nama class |

Contoh:

```yaml
train: /content/data_prepared/train/images
val: /content/data_prepared/valid/images
test: /content/data_prepared/test/images

nc: <jumlah kelas>

names:
  - ...
```

---

## 🔍 Quality Control

Notebook menyediakan fungsi `quick_qc()` untuk mengambil sample gambar dan menampilkan bounding box hasil auto-labeling.

```python
quick_qc("train", n=6)
```

### Pemeriksaan QC

| Pemeriksaan | Tujuan |
|---|---|
| **Bounding box** | Memeriksa posisi dan cakupan objek |
| **Class** | Memeriksa class hasil auto-labeling |
| **Label consistency** | Menemukan label yang tidak sesuai |
| **Visual inspection** | Memastikan dataset layak digunakan sebelum training |

---

## 📈 Model Evaluation

Setelah training selesai, model divalidasi menggunakan:

```python
metrics = model.val()
```

### Evaluation Metrics

| Metric | Keterangan |
|---|---|
| **Precision** | Proporsi prediksi positif yang benar |
| **Recall** | Proporsi objek yang berhasil terdeteksi |
| **mAP50** | Mean Average Precision pada IoU 0.50 |
| **mAP50-95** | Mean Average Precision pada IoU 0.50–0.95 |

Hasil dapat ditampilkan dengan:

```python
print("mAP50:", metrics.box.map50)
print("mAP50-95:", metrics.box.map)
```

### Validation Result

| Metric | Result |
|---|---:|
| **Precision** | **89.3%** |
| **Recall** | **84.1%** |
| **mAP50** | **89.6%** |
| **mAP50-95** | **83.5%** |

| Validation Dataset | Value |
|---|---:|
| **Images** | 187 |
| **Instances** | 248 |
| **Background** | 1 |
| **Corrupt** | 0 |

### Per-Class Validation Result

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|
| Apple | 88.2% | 93.3% | 94.9% | 93.8% |
| Banana | 96.5% | 77.4% | 88.3% | 75.8% |
| Grapes | 92.4% | 75.8% | 87.5% | 73.1% |
| Kiwi | 94.3% | 100.0% | 95.6% | 94.0% |
| Mango | 100.0% | 91.7% | 97.8% | 95.4% |
| Orange | 69.4% | 68.6% | 72.9% | 63.7% |
| Pineapple | 73.3% | 71.0% | 74.9% | 64.1% |
| Sugerapple | 94.8% | 100.0% | 99.5% | 99.5% |
| Watermelon | 94.6% | 79.1% | 94.9% | 92.3% |

> **Evaluation note:** Angka di atas merupakan hasil **validation** dari run yang tersedia. Training metrics dan independent test metrics tidak dicantumkan sebagai angka karena tidak tersedia pada output evaluasi yang digunakan untuk dokumentasi ini.

---

## 📦 Model

### Model Training

| Item | Detail |
|---|---|
| **Training Model** | YOLO26n |
| **Best Weights** | `best.pt` |
| **Exported Model** | `yolo26n_models.pt` |

### Model Location

| Location | Path |
|---|---|
| **Local Project** | `models/yolo26n_models.pt` |
| **Google Drive** | `MyDrive/Projek/Fruits Detection (Object Detection)/models/yolo26n_models.pt` |

---

## 🖼️ Inference

Inference dapat dijalankan secara lokal menggunakan:

```text
inference.py
```

### Input Images

| File | Location |
|---|---|
| `1.jpg` | `images/1.jpg` |
| `2.jpg` | `images/2.jpg` |
| `3.jpg` | `images/3.jpg` |
| `4.jpg` | `images/4.jpg` |
| `pisang.jpg` | `images/pisang.jpg` |

### Model

| Item | Path |
|---|---|
| **Model** | `models/yolo26n_models.pt` |

### Run

```bash
python inference.py
```

### Inference Configuration

| Parameter | Value |
|---|---|
| **Model Path** | `models/yolo26n_models.pt` |
| **Image Path** | `images/2.jpg` |
| **Confidence Threshold** | `0.4` |

Contoh:

```python
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

---

## ☁️ Google Drive Export

Notebook menggunakan Google Drive untuk menyimpan model hasil training:

```python
from google.colab import drive

drive.mount('/content/drive')
```

### Export Location

| Item | Path |
|---|---|
| **Destination** | `MyDrive/Projek/Fruits Detection (Object Detection)/models/yolo26n_models.pt` |
| **Filename** | `yolo26n_models.pt` |

---

## ⚠️ Keterbatasan

- Training dilakukan di Google Colab karena komputer lokal tidak menggunakan GPU dedicated.
- Waktu training dapat berbeda tergantung resource GPU Google Colab yang tersedia.
- Hasil auto-labeling bergantung pada kemampuan model `yolov8s-worldv2`.
- Fallback bounding box digunakan ketika class diketahui dari `_classes.csv`, tetapi objek tidak berhasil ditemukan oleh labeler.
- Metric dapat berbeda apabila proses training dijalankan kembali.
- Versi Python, PyTorch, CUDA, dan Ultralytics dapat memengaruhi kompatibilitas serta performa.
- Karena sebagian label diperoleh melalui proses auto-labeling, hasil validation tidak dapat dianggap sebagai evaluasi terhadap ground-truth manual yang sepenuhnya independen.

---

## 👤 Credits

**Puteri Amelia Azli**

Project / notebook dibuat pada:

**16 September 2026**

### Portfolio

- GitHub: https://github.com/puteriazli
- LinkedIn: https://www.linkedin.com/in/puteriazli
- Kaggle: https://www.kaggle.com/puteriameliaazli
- YouTube: https://www.youtube.com/@putericoding
