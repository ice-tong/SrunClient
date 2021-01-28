# SrunClient
简易版深澜命令行客户端，包含登录登出和查询在线信息功能。支持 windows/Linux/?MacOS，python2/3 。 包含校园内网服务器反向代理教程。

# how to use 
1. 使用命令行客户端登录登出
    更换`srun_ip`为自己学校对应的深澜网关地址
    ``` python3
    class SrunClient:

        name = 'CUGB'
        srun_ip = '202.204.105.195' # or srun_ip = 'gw.cugb.edu.cn'

        login_url = 'http://{}/cgi-bin/srun_portal'.format(srun_ip)
        online_url = 'http://{}/cgi-bin/rad_user_info'.format(srun_ip)
        headers = {'User-Agent': 'SrunClient {}'.format(name)}

    ``` 
    然后运行srun.py 
    ``` 
    [user@host SrunClient]$ python srun.py
    ############### Wellcome to Srun Client ###############
    [1]: show online information
    [2]: set username and passwd
    [3]: login
    [4]: logout
    [h]: show this messages
    [q]: quit
    #######################################################
    [SrunClient CUGB] ###*** NOT ONLINE! ***###
    >
    ```

2. 掉线自动重连 
    - 🍬**推荐**🍬 定时任务，定时执行heartbeat.py。   
        使用crontba添加定时任务
        ```shell
        [user@host SrunClient]$ crontab -e
        ```   
        将下列命令添加，按`esc`，输入`:wq`退出保存（每分钟执行一次命令）。
        ```
        * * * * * python /path/to/heartbeat.py
        ```
    - 或配合`nohup`使用，每隔10秒钟检测一次在线情况，不在线则重新登录。在`heartbeat.py`中设置好登录账号和密码之后，运行：
        ```shell
        nohup python heartbeat.py &
        ```   
        `nohup` 进程有被杀死的风险
 
# addition

- [SSH反向代理 内网穿透](./sshr_readme.md)

# to do

- [ ] 定时下线
- [ ] 更换ip
