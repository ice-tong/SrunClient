from srun import SrunClient
import socket
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(filename)s:%(lineno)d] %(message)s',
    datefmt='## %Y-%m-%d %H:%M:%S'
)
logging.getLogger("heartbeat").setLevel(logging.INFO)
logger = logging.getLogger("heartbeat")

USERNAME = ''
PASSWD = ''

CHECK_SERVER = 'www.baidu.com'


def check_connect():
    with socket.socket() as s:
        s.settimeout(3)
        try:
            status = s.connect_ex((CHECK_SERVER, 443))
            return status == 0
        except Exception as e:
            print(e)
            return False


def check_online():
    if check_connect(): return
    srun_client = SrunClient(print_log=False)
    # Use this method frequently to check online is not suggested!
    # if srun_client.check_online(): return
    logger.info('NOT ONLINE, TRY TO LOGIN!')
    srun_client.username = USERNAME
    srun_client.passwd = PASSWD
    srun_client.login()


if __name__ == "__main__":
    check_online()
    
#     import time
#     while 1:
#         check_online()
#         time.sleep(10)
