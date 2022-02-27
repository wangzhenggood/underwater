import jenkins
jenkins_server_url='xxx'
user_id='xxx'
password='xxxxx'  #password是密钥

def get_node():                                                 #获取jenkins的节点
    jenkins_servers=jenkins.Jenkins('xxx'+jenkins_server_url,username=user_id,password=password)
    nodes=jenkins_servers.get_nodes()                           #获取到jenkins节点的数据
    link=[]
    not_link=[]
    for count in range(0,len(nodes)):                           #拆分自己需要的数据
        if nodes[count]['offline'] is False:                    #这里主要是连接的节点，遍历得到我们想要的数据，加入列表中
            link.append(nodes[count]['name'])
        else:
            not_link.append(nodes[count]['name'])                                #未连接的节点
    for node in not_link:
        if node.__contains__('Pass') or node.__contains__('test'):               #__contains__方法主要是设置过滤
            jenkins_servers.delete_node(node)                                    #获取过滤得到的东西进行删除操作
            print(node)
        return not_link

def crate_node():                                              #创建新的节点
    not_link=get_node()                                        #调用get_node方法的返回值
    for new_node in not_link:                                  #遍历列表进行批量添加
        print(new_node)
        jenkins_server=jenkins.Jenkins('xxx'+jenkins_server_url,username=user_id,password=password)
        jenkins_server.create_node(                            #添加节点需要的相关参数，java_web启动的话就只需要这些参数
            name=new_node,
            numExecutors=3,
            remoteFS='/passdata/jenkins',
            launcher=jenkins.LAUNCHER_JNLP,
        )

if __name__ == '__main__':
        get_node()