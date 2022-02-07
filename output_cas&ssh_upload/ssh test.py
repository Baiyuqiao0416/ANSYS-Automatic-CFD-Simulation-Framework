from distutils import command
import paramiko #third package
from scp import SCPClient #third package
import sys
import time

host='10.30.76.17'
user='gengzi'
passw='gengzi123'
filepath0=sys.path[0]+'\\1_2.00mm.cas.gz'
filepath1=sys.path[0]+'\\1_2.00mm.dat.gz'
filepath2=sys.path[0]+'\\journal.jou'
filepath3=sys.path[0]+'\\sub.slurm'
remotefilepath='/home/gengzi/zxy/6L2500rpm'
localfilepath='E:\\py_on_workbench'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, port=22, username=user, password=passw)
channel = ssh_client.invoke_shell()  #变成交互性终端

# while 1:
#     command = input(">>")
#     channel.send(command + "\n")  #加\n代表回车执行命令
#     time.sleep(1)  #执行命令后结果返回可能有延迟，为了保证结果都到缓冲区，最好暂停一下
#     buf = channel.recv(10024).decode("utf-8")
#     print(buf)

#get cpu_free
# command=('top -bn 1 -i -c')
# channel.send(command + "\n")  
# time.sleep(1)  
# buf = channel.recv(10024).decode("utf-8")
# text=buf.split('\n')
# text2=text[4].split(' ')
# cpu_free=text2[10]

#upload
def upload(LOCAL_FILE_PATH,SERVER_REMOTE_PATH):
    scp_client = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    try:
        scp_client.put(LOCAL_FILE_PATH, SERVER_REMOTE_PATH)
    except FileNotFoundError as e:
        print(e)
    else:
        print("upload successfully!")
    scp_client.close()

#download
def download(LOCAL_FILE_PATH,SERVER_REMOTE_PATH):
    scp_client = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)
    try:
        scp_client.get(SERVER_REMOTE_PATH, LOCAL_FILE_PATH)
    except FileNotFoundError as e:
        print(e)
    else:
        print("download successfully!")
    scp_client.close()

upload(filepath0,remotefilepath)
upload(filepath1,remotefilepath)


input()
