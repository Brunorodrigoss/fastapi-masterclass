import datetime
from fastapi.requests import Request

def log(tag="MyApp", message="", request: Request= None):
    with open("log.txt", "a+") as log:
        log.write(f'[{datetime.datetime.now()}] {tag}: {message} \t{request.url} \n')