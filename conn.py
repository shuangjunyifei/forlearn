import pymysql
def convert_test_dic(name):
    conn = pymysql.Connect(host='localhost',port=3306,user='test',passwd='test',db='testdb',charset='utf8')
    cursor = conn.cursor()
    sql="select * from "+name
    cursor.execute(sql)
    results=cursor.fetchall()
    name={}
    for row in results:
        name[row[0]]=row                           #接下来就是循环构造结构
    print(name)
    return(name)
    cursor.close()
    conn.close()
