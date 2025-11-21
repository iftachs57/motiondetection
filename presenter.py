import time

import cv2

import consts


def present(images):
    while True:
        item = images.get()
        if item is None:
            break

        frame, detections = item

        for (x, y, w, h) in detections:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        timestamp = time.strftime(consts.Time_struct)
        cv2.putText(frame, timestamp, (10, 25), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)

        cv2.imshow(consts.Windows_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
