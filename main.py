from consts import Q1_size, Q2_size
from streamer import stream
from detector import detect
from presenter import present

from multiprocessing import Process, Queue

if __name__ == "__main__":
    video_url = ""

    q1 = Queue(maxsize=Q1_size)
    q2 = Queue(maxsize=Q2_size)

    p1 = Process(target=stream, args=(video_url, q1))
    p2 = Process(target=detect, args=(q1, q2))
    p3 = Process(target=present, args=(q2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
