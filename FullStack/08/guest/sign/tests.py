from django.test import TestCase
import pymysql.cursors
# Create your tests here.
connection = pymysql.connect(host = '127.0.0.1', user = 'root' ,password = '123456',
                             db ='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'
        cursor.execute(sql)
        connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()