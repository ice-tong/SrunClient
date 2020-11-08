# SrunClient
简易版深澜客户端，包含登录登出和查询在线信息功能。支持 windows/Linux，python2/3 。

# how to use
更换自己学校对应的深澜网关地址
``` python3 
class SrunClient:
    
    name = 'CUGB'
    srun_ip = '202.204.105.195' # or srun_ip = 'gw.cugb.edu.cn'

    login_url = 'http://{}/cgi-bin/srun_portal'.format(srun_ip)
    online_url = 'http://{}/cgi-bin/rad_user_info'.format(srun_ip)
    headers = {'User-Agent': 'SrunClient {}'.format(name)}
``` 
然后运行srun.py
`python srun.py`

# to do

- 定时下线
