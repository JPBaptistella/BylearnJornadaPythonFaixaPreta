from CLO.database.manager import search_CLLB_Tarefa_Diaria, search_CLLB_Tarefa_Semanal, search_CLLB_Tarefa_Mensal
from CLO.utils import dia_da_semana, data_atual

semana=dia_da_semana()

def initialize(Menu_CLL):
    from CLO.cl_limpeza.cl_limpeza_bar import Tela_CLLB

    tcllb=Tela_CLLB(Menu_CLL)
    tcllb.enable_window()

def load_TLDB():
    
    TLDB = search_CLLB_Tarefa_Diaria()
    TLDB = [_atividade[0] for _atividade in TLDB]

    for tarefa in TLDB:
        return TLDB

def load_TLSB():

    TLSB=search_CLLB_Tarefa_Semanal()
    TLSB=[_atividade[0] for _atividade in TLSB]
    
    for tarefa in TLSB:
        if semana == 'Monday':
            return 'Segunda', TLSB[0]
        elif semana == 'Tuesday':
            return 'Terça:', TLSB[1]
        elif semana == 'Wednesday':
            return 'Quarta: ',TLSB[2]
        elif semana == 'Thursday':
            return 'Quinta:', TLSB[3]
        elif semana == 'Friday':
            return 'Sexta:', TLSB[4]
        elif semana == 'Saturday':
            return 'Sábado', TLSB[5]
        else:
            return 'Domingo'

def load_TLMB():

    TLMB=search_CLLB_Tarefa_Mensal()
    TLMB=[_atividade[0] for _atividade in TLMB]

    for tarefa in TLMB:
        if data_atual == '1':
            return 'A tarefa mensal é:', TLMB[0]
        elif data_atual == '15':
            return 'A tarefa mensal é:', TLMB[1]
        else:
            return 'Não há tarefas mensais hoje'



