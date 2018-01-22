import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='test',passwd='test',db='testdb',charset='utf8')
cursor = conn.cursor()
sql="*****(标准SQL语句)"

cursor.execute(sql)


接下来就是循环构造结构



cursor.close()
conn.close()
