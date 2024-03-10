from prefect import flow, task
import requests
import json 

def log(level: int, msg: str):
    
    if not level:
        log_level = "message"
    else:
        log_level = "error"
    
    print("[{0}]: {1}".format(log_level, msg))

@task
def do_request(url: str):
    try:
        res = requests.get(url)

        if res.status_code == 200:
            res = res.text

        log(0, "proccess completed")
    except:
        res = ""
        log(-1, "process uncompleted")
    
    return res

@task
def do_parse(res):
    try:
        data = json.loads(res)
        log(0, "parse completed")
    except:
        data = ""
        log(-1, "parse process failed")

    return data

@task
def do_print(data):
    try:
        print("[data]: ", end="")
        print(data)
        log(0, "print completed")
    except:
        log(-1, "print process failed")

@flow
def main_flow():
    do_print(do_parse(do_request("https://jsonplaceholder.cypress.io/todos/1")))

if __name__ == '__main__':
    main_flow()