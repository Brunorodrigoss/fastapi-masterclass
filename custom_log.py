import datetime

def log(tag="", message=""):
    with open("log.txt", "a") as log:
        log.write(f'[{datetime.datetime.now()}] {tag}: {message}\n')