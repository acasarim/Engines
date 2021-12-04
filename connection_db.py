import mysql.connector
from mysql.connector import errorcode

class Database:

    def __init__(self):
        self.__db_con = mysql.connector.connect(host='',
                                                user='',
                                                password='',
                                                database='')

    def conectar(self) -> str:
        try:
            self.__db_con
            print('CONEXÃO ABERTA')
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                 print("DATABASE DOESN'T EXIST!")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("USER NAME OR PASSWORD IS WRONG")
            else:
                print("error")
              
    def desconectar(self) -> str:
        self.__db_con.close()
        print('CONEXÃO FECHADA')
