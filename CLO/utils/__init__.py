import PySimpleGUI as sg
import os
import sys
import datetime

def inner_element_space(width=100):
    return [sg.Text(' '*width, font=('Arial',1))]

def root_folder():
    if getattr(sys, "frozen", False): 
        return os.path.dirname(sys.executable)

    try:
        main_file = os.path.abspath(sys.modules['__main__'].__file__)
    except:
        main_file = sys.executable

    return os.path.join(os.path.dirname(main_file), os.pardir)

def verificador_data():
    dia_hoje = datetime.today().strftime('%A')
    data_atual= datetime.today()
    data_atual='{}'.format(data_atual.day)