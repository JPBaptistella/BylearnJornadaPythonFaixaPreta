from CLO.database.manager import search_CLLB_Tarefa_Diaria, search_CLLB_Tarefa_Semanal, search_CLLB_Tarefa_Mensal


def initialize(Menu_CLL):
    from CLO.cl_limpeza.cl_limpeza_bar import Tela_CLLB

    tcllb=Tela_CLLB(Menu_CLL)
    tcllb.enable_window()

def load_TLDB():
    
    TLDB = search_CLLB_Tarefa_Diaria()
    TLDB = [_atividade[0] for _atividade in TLDB]

    return TLDB

def load_TLSB():

    TLSB=search_CLLB_Tarefa_Semanal()
    TLSB=[_atividade[0] for _atividade in TLSB]

    return TLSB

def load_TLMB():

    TLMB=search_CLLB_Tarefa_Mensal()
    TLMB=[_atividade[0] for _atividade in TLMB]

    return TLMB


