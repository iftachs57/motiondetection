import cv2


def detect(images, procesed_images):
    back = cv2.createBackgroundSubtractorMOG2()

    while True:
        frame = images.get()
        if frame is None:
            procesed_images.put(frame)
            break
        image = back.apply(frame)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        rects = []
        for c in contours:
            if cv2.contourArea(c) > 500:
                x, y, w, h = cv2.boundingRect(c)
                rects.append((x, y, w, h))

        procesed_images.put((frame, rects))
