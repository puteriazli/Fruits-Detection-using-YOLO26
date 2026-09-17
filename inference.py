import cv2
from ultralytics import YOLO

MODEL_PATH = "models/yolo26n_models.pt"
IMAGE_PATH = "images/2.jpg"
CONF_THRESHOLD = 0.4

# GitHub: https://github.com/puteriazli

model = YOLO(MODEL_PATH)
result = model.predict(source=IMAGE_PATH, conf=CONF_THRESHOLD, verbose=False)[0]
annotated_frame = result.plot()

cv2.imshow("Detection Result", annotated_frame)
print("Tekan tombol apa saja di jendela gambar untuk menutup...")
cv2.waitKey(0)
cv2.destroyAllWindows()