import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='users',
                                  charset='utf8')
        self.cur = self.db.cursor()


    def registration_method(self,name,password):
        sql = "insert into name from user where name=%s;"% name
        self.cur(sql,[name])
        tur = self.cur.fetchone()
        if not tur:
            return False

        try:
            sql = "insert into  from "









if __name__ == '__main__':
    db = Database()
    db.registration_method()
    db.Login_method()
