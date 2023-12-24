import multiprocessing

def multproc(target,urls):
    processes = []
    for i in range(len(urls)):
        p= multiprocessing.Process(target=target, args=(urls[i],))

        processes.append(p)
        p.start()

    for t in processes:
        t.join()