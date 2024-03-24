import cv2
import time
from detect_faces import detect_faces_mobilenetssd
import av
import math

n_frames = 0
fps_cum = 0.0
fps_avg = 0.0

def callback1(frame):
    global n_frames,fps_cum,fps_avg
    frame=frame.to_ndarray(format="bgr24")
    model_prototxt = 'MobileNetSSD_deploy.prototxt'
    model_weights = 'MobileNetSSD_deploy.caffemodel'
    net = cv2.dnn.readNetFromCaffe(model_prototxt, model_weights)
    start_time = time.perf_counter()
    n_frames+=1

    frame, face_count = detect_faces_mobilenetssd(frame.copy(), net)

    cv2.putText(frame, f"Live Face Count: {face_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    end_time = time.perf_counter()
    fps = 1.0 / (end_time - start_time)
    fps_cum += fps
    fps_avg = fps_cum / n_frames
    cv2.putText(frame, f"FPS: {math.ceil(fps_avg)}", (10, 60),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    
    return av.VideoFrame.from_ndarray(frame,format="bgr24")
