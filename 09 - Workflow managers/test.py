from prefect import Flow, task

@task
def get_message():
    message = "Hello"
    return message

@task
def log_message(message):
    print("message: " + message)

@flow
def main_flow():
    message = get_message()
    log_message(message)

if __name__ == '__main__':
    main_flow()