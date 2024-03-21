import cv2
import numpy as np

def detect_faces_mobilenetssd(frame, net):
    blob = cv2.dnn.blobFromImage(frame, 1.0/127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True)
    net.setInput(blob)
    detections = net.forward()

    face_count = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Adjust confidence threshold
            class_id = int(detections[0, 0, i, 1])
            if class_id == 15:  # 15 should be the class ID for faces
                box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (x, y, x2, y2) = box.astype("int")

                cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
                face_count += 1

    return frame, face_count