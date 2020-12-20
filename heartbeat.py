from srun import SrunClient
import time
import getpass
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(filename)s:%(lineno)d] %(message)s',
    datefmt='## %Y-%m-%d %H:%M:%S'
)
logging.getLogger("heartbeat").setLevel(logging.INFO)
logger = logging.getLogger("heartbeat")

time_interval = 10 # 10s

#USERNAME = input('username: ')
#PASSWD = getpass.getpass('passwd: ')
USERNAME = ''
PASSWD = ''

def check_online():
    srun_client = SrunClient(print_log=False)
    if srun_client.check_online(): return
    logger.info('NOT ONLINE, TRY TO LOGIN!')
    srun_client.username = USERNAME
    srun_client.passwd = PASSWD
    srun_client.login()


def main(): ...


if __name__ == "__main__":
    while 1:
        check_online()
        time.sleep(time_interval)
