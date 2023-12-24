import threading
from main import *


def thread(target,urls):
    threads = []
    for i in range(len(urls)):
        t= threading.Thread(target=target, args=(urls[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
