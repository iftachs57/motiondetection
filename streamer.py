import cv2

def stream(video, queue):
    cap = cv2.VideoCapture(video)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        queue.put(frame)
    queue.close()
    cap.release()