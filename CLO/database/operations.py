#Operações Gerais do banco de dados

import sqlite3

def create(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print('Ops... Deu um erro criando uma tabela:', error)

def select(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
    except sqlite3.Error as error:
        print('Ops... Deu um erro buscando um dado:', error)
    finally:
        return result