from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov8n.pt")

image_path = "image.jpg"
img = cv2.imread(image_path)

results = model(image_path)

boxes = results[0].boxes.xyxy.cpu().numpy()
classes = results[0].boxes.cls.cpu().numpy()

overlay = cv2.imread("overlay.png", cv2.IMREAD_UNCHANGED)

for i, box in enumerate(boxes[:2]):
    x1, y1, x2, y2 = map(int, box)
    roi = img[y1:y2, x1:x2]
    overlay_resized = cv2.resize(overlay, (x2 - x1, y2 - y1))

    if overlay_resized.shape[2] == 4:
        alpha_s = overlay_resized[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(3):
            roi[:, :, c] = (alpha_s * overlay_resized[:, :, c] + alpha_l * roi[:, :, c])
    else:
        roi[:] = overlay_resized

    img[y1:y2, x1:x2] = roi

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result.jpg", img)
