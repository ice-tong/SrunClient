# SSH 反向代理 内网穿透 

- ### 基本原理  
  内网主机没有公网ip，在外网中无法直接通过公网ip来连接内网主机。  
  让内网主机向有公网ip的外网主机发起ssh请求，并建立起隧道连接。  
  此时外网主机和内网主机有一条通信隧道，便可以通过这条隧道进行ssh连接，而不用知道内网主机的ip。  

- ### *内网主机A* : A_user@A_host  
- ### *外网主机B* : B_user@B_host


## 内网主机A 操作步骤（大概步骤）

1. 确保内网主机一直在线（optional）  
  设置定时任务执行heartbeat.py  
  或修改heartbeat.py，循环检测掉线，使用`nohup`执行
  `nohup python heartbeat.py &`  
  不断检测网络在线情况，防止掉线。 （heartbeat.py中填入登录账户和密码）

2. ssh设置免密登录   
  `ssh-keygen`  
  `ssh-copy-id B_user@B_host`  

3. 使用autossh反向代理   
  `autossh -M 4010 -fCNR 1024:localhost:22 B_user@B_host`  
  autossh的作用类似于不挂断的进行ssh连接   
  ```
  -M 4010 置autossh的监听端口为4010  
  -fCNR  
    -f 让ssh在后台执行命令  
    -C 允许压缩数据  
    -N 只进行端口转发，不执行远程指令  
    -R 远程主机的端口转发到本地端口 （反向代理）  
    -L 本地端口转发到远程主机端口 （正向代理）  
  1024:localhost:22  
    1024 远程主机端口  
    22 本地端口 （ssh默认端口） 
  ```


4. 设置开机自启  
  将网络在线检测以及autossh反向代理命令添加到开机自启   
  `sudo vi /etc/rc.d/rc.local`
  将下列命令填入开机自启文件 /etc/rc.d/rc.local    
  ```
  nohup python /path/to/heartbeat.py &
  autossh -M 4010 -fCNR 1024:localhost:22 B_user@B_host
  ```   

## 外网主机B 操作流程 

- 在外网主机B上，通过  
  `ssh A_user@localhost -p 1024`  
  可以登录到内网主机上。  

-  或者  
  `ssh -fCNL  *:2048:localhost:1024 localhost`  
  将本地的1024端口转发到本地的2048端口  
  如此可实现在任意终端上，通过外网主机B的代理，连接上内网主机A  
  `ssh A_user@B_host -p 2048`  
