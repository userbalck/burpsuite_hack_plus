import os
import sqlite3

SqliPath=''
#创建表
def insta_crate_database(script_dir):
    global  SqliPath
    DB_FILE_PATH = script_dir + '/' + 'burphack.db'
    SqliPath=DB_FILE_PATH
    print(DB_FILE_PATH)
    # 检查数据库文件是否存在
    if not os.path.exists(DB_FILE_PATH):
        # 连接到 SQLite 数据库（如果数据库文件不存在，会自动创建）
        conn = sqlite3.connect(DB_FILE_PATH)
        cursor = conn.cursor()
        # 判断创建的表不存在则创建
        # 创建 sql_bool 表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS sql_bool (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           host TEXT NOT NULL,
                           risk INTEGER NOT NULL,
                           bool_true_resp TEXT NOT NULL,
                           bool_true_req TEXT NOT NULL,
                           bool_false_resp TEXT,
                           bool_false_req TEXT,
                           first_resp TEXT NOT NULL,
                           payload TEXT NOT NULL,
                           first_req TEXT NOT NULL,
                           create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       );
                       ''')

        # 创建 sql_error 表
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS sql_error (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           request_data TEXT,
                           response TEXT,
                           host TEXT,
                           dbms TEXT,
                           create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       );
                       ''')
        # 创建 ssrf 表
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS ssrf (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        payload TEXT,
                        request_data TEXT,
                        response TEXT,
                        host TEXT,
                        is_vul INTEGER DEFAULT 0,
                        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        vuType INTEGER
                    );
                    ''')
        conn.commit()
        conn.close()
        print("数据库和表创建成功！")

    else:
        print("数据库文件已存在，无需创建。")

def get_conn():
    global SqliPath
    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
    如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
    路径下的数据库文件的连接对象；否则，返回内存中的数据接
    连接对象'''
    conn = sqlite3.connect(SqliPath)
    cur = conn.cursor()
    if os.path.exists(SqliPath) and os.path.isfile(SqliPath):
        # print('硬盘上面:[{}]'.format(SqliPath))
        return conn,cur
    else:
        conn = None
        # print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')


def insert_err(request_data,response,host,dbms_type):
    conn, cur = get_conn()
    # 使用参数化查询构造 SQL 语句
    sql = "INSERT INTO sql_error (`request_data`, `response`, `host`, `dbms`) VALUES (?, ?, ?, ?)"
    try:
        # 执行插入操作
        cur.execute(sql, (request_data, response, host, dbms_type))
        conn.commit()  # 提交事务
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接

def insert_exec(sql,data):
    '''
    执行插入，sql预编译语句，data数据
    '''
    conn, cur = get_conn()
    # 使用参数化查询构造 SQL 语句

    try:
        # 执行插入操作
        cur.execute(sql, data)
        conn.commit()  # 提交事务
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接


def insert_data(sqldata):
    print(sqldata)
    conn,cur=get_conn()
    try:
        # 执行插入操作
        cur.execute(sqldata)
        conn.commit()  # 提交事务
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库连接

def GetSelect(sqldata):
    print(sqldata)
    conn,cur=get_conn()
    try:
        # 执行插入操作
        curosor=cur.execute(sqldata)
        # 获取所有结果
        items = curosor.fetchall()
        return items  # 返回结果
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
    finally:
        cur.close()  # 关闭游标



# if __name__ == '__main__':
#     dbsqli=DBsqli()
#     dbsqli.insta_crate_database()
