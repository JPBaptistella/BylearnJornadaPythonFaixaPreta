
from CLO.database.connector import close_connection, connect
from CLO.database.operations import select

#SELECT * FROM CLLB;
#SELECT atividade FROM CLLB WHERE Peridiocidade = "D";
#SELECT atividade FROM CLLB WHERE Peridiocidade = "S";
#SELECT atividade FROM CLLB WHERE Peridiocidade = "M";

def search_CLLB():
    connection = connect()

    sql = "SELECT * FROM CLLB;"
    CLLB = select(connection, sql)

    close_connection(connection)

    return CLLB

def search_CLLB_Tarefa_Diaria():
    connection = connect()

    sql = "SELECT atividade FROM CLLB WHERE periodicidade='D'"
    CLLB_Tarefa_Diaria = select(connection,sql)

    close_connection(connection)

    return CLLB_Tarefa_Diaria