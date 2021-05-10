import threading


# Creating threads
def create_threads(links, save_path, function):
    threads = []

    for video in links:
        th = threading.Thread(
            target=function, args=(video, save_path)
        )  # args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
