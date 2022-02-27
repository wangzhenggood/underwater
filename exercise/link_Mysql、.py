import pymysql
conn=pymysql.connect(host='localhost',                 #本机  IP
                     user='root',                      #账号
                     password='root',                   #密码
                     db='MySQL1',                     #数据库名
                     charset='utf-8',
                     cursorclass=pymysql.cursors.DictCursor)        #游标类      DictCursor ：光标

#打开数据库连接，参数1 ：主机名或IP;参数2：用户名
db=pymysql.connect('localhost','root','root','studyPython')
#使用cursor（）方法创建一个游标对象cursor
cursor=db.cursor()
#使用execute()方法执行SQL查询
cursor.execute('SELECT VERSION()')
#使用fetchone()方法获取单条数据
data=cursor.fetchone()
print('Database version :%s'%data)
#关闭数据库连接
db.close()

#打开数据库连接，参数1 ：主机名或IP;参数2：用户名
db=pymysql.connect('localhost','root','root','studyPython')
#使用cursor（）方法创建一个游标对象cursor
cursor=db.cursor()
#使用execute（）方法执行SQL，如果表存在，则删除
cursor.execute('DROP TABLE IF EXISTS books')
#使用预处理语句创建表
sql='''
CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    PRIMARY KEY(id) 
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSENT=utf-8;
'''
#执行sql语句
cursor.execute(sql)
#关闭数据库连接
db.close()

#打开数据库连接
db=pymysql.connect('localhost','root','root','mrsoft',charset='utf-8')
#使用cursor（）方法获取操作游标
cursor=db.cursor()
#数据列表
data=[
    ('1','2','3','4','5'),
    ('1','2','3','4','5'),
    ('1','2','3','4','5'),
]
try:               #执行sql语言，插入多条数据
    cursor.executemany('insert into books(name,categoty,price,publish_time) values(%s,%s,%s,%s)',data)
    #提交数据
    db.commit()
except:
    #发生错误时回滚
    db.rollback()

#关闭数据库
db.close()
