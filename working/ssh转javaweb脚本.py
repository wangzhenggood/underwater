import jenkins    #安装 pip install python-jenkins
import argparse
import time
from retrying import retry

jenkins_server_url='https://xxx.com.cn'
user_id='用户名xxx'
'''连接到jinkins服务器 url：所连接的jenkins的网络地址  username用户名  password密码
   获取所有的job信息：server.get_jobs()
   获取job为name的基本信息：server.get_job_info(name)
   正则匹配到响应的job基本信息：server.get_job_info_regex(pattern)
   判断job是否存在：server.job_exists(name)
   获取所有job的数量：server.jobs_count()
-----------------------------------------------
   所谓build的话，指的是在Job里面的一次构建
   获取所有排队的build: server.get_queue_info()
   获取所有正在运行的build: server.get_running_builds()
   停止正在运行的构建: server.stop_build(name, number)
'''
jenkins_servers=[jenkins.Jenkins(jenkins_server_url+'central-zenzap',username=user_id,password='xxxx'),
                 jenkins.Jenkins(jenkins_server_url+'research-otcp',username=user_id,password='xxxx')]
#
def parse_args():       #解析参数
    '''1、创建一个解析器——创建 ArgumentParser() 对象
       2、添加参数——调用 add_argument() 方法添加参数
       3、解析参数——使用 parse_args() 解析添加的参数'''
    parser=argparse.ArgumentParser()   #parser 分析程序    argparse命令行解析模块  ArgumentParser 参数
    parser.add_argument('-C','--controller_ip',help='paas controller ip for create pass slave node',required=False)   #argument 论证 参数  required：必须
    parser.add_argument('-P','--jdk_path',help='jdk path info',required=False)
    return parser.parse_args()            #解析器 解析参数
@retry(stop_max_attempt_number=5)         #retry 重试  stop_max_attempt_number 停止最大尝试次数
def create_pass_slave_node(controller_ip,jdk_path,jenkins_server):  #controller_ip：控制器ip  node ：节点
    try:
        time.sleep(10)
        pass_node='PASS_'+controller_ip
        if jenkins_servers.node_exists(pass_node):         #节点存在
            print('begin to delete jenkins slave node:'+pass_node)   #通过节点
            jenkins_servers.delete_node(pass_node)          #删除节点
            time.sleep(5)
        print('begin to create jenkins slave node:'+pass_node)         #开始创建从节点
        params=[]                                        # params参数
        params['host']=controller_ip                     #host 主机
        params['port']=22                                #port 端口
        params['credentialsld']='xxxxx'                  #credentialsld 受信任的凭证
        params['javaPath']=jdk_path
        jenkins_server.create_node(
            pass_node,                                   #通过节点
            numExecutors=3,                              #数字执行器
            nodeDescription='c',                         #节点描述
            remoteFS='/paasdata/jenkins',                #远程      paas 平台即服务
            labels=controller_ip,                        #标签
            exclusive=True,                              #独有的
            launcher=jenkins.LAUNCHER_SSH,               #发射器
            launcher_params=params                       #启动参数   发送参数
             )
        print('create jenkins slave node sucess:'+pass_node)
        time.sleep(5)
    except Exception as e:                               #Exception：例外
        print(e)
        raise e             #通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行

if __name__ == '__main__':
    args=parse_args()
    if args.jdk_path:
        jdk_path=args.jdk_path
    else:
        jdk_path='/passdata/op-data/openjdk/openjdk8u181/bin/java'
    if args.controller_ip:
        for jenkins_server in 'jenkins_servers':                             #原本是Jenkins_servers 我没有这个内容
            create_pass_slave_node(args.controller_ip,jdk_path,jenkins_server)