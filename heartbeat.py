from srun import SrunClient
import time


time_interval = 60*10


def check_online():
    srun_client = SrunClient()
    if srun_client.check_online(): return
    srun_client.username = 'username'
    srun_client.passwd = 'passwd'
    srun_client.login()


def main(): pass


if __name__ == "__main__":
    while 1:
        check_online()
        time.sleep(time_interval)
        
