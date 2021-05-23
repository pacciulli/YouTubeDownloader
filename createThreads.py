import threading


# Creating threads
def create_threads(links, save_path, function, resolution):
    threads = []

    for video in links:
        th = threading.Thread(target=function, args=(video, save_path, resolution))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
