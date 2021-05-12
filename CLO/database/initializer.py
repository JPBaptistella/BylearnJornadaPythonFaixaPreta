#Inicializar e criar o banco na primeira vez
from CLO.database.connector import close_connection, connect
from CLO.database.operations import create

def initialize():
    connection = connect()

    sql_create_table_CLLB = """ CREATE TABLE IF NOT EXISTS CLLB(
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    Atividade text NOT NULL,
                                    Periodicidade text NOT NULL
                                );"""
        
    create(connection,sql_create_table_CLLB)

    close_connection(connection)