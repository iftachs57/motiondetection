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
            part = frame[y:y + h, x:x + w]
            blurred = cv2.GaussianBlur(part, (consts.Blurx, consts.Blury), 0)
            frame[y:y + h, x:x + w] = blurred
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (consts.Ditect_rect_color_B, consts.Ditect_rect_color_G, consts.Ditect_rect_color_R), 2)

        timestamp = time.strftime(consts.Time_struct)
        cv2.putText(frame, timestamp, (10, 25), cv2.FONT_HERSHEY_PLAIN, consts.Time_font_size,
                    (consts.Time_color_B, consts.Time_color_G, consts.Time_color_R), consts.Time_thickness)

        cv2.imshow(consts.Windows_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
