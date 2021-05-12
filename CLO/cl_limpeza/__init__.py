import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from CLO.cl_limpeza import  view
from CLO.cl_limpeza.cl_limpeza_bar.manager import initialize as init_Tela_CLLB
from CLO.cl_limpeza.cl_limpeza_salao.manager import initialize as init_Tela_CLLS
from CLO.cl_limpeza.cl_limpeza_salao.manager import initialize as init_Tela_CLLC

class Menu_CLL:
    def __init__(self, Menu):
        self.window = None
        self.menu=Menu
        
    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()
    
    def enable_window(self):
        self.instantiate()
    
        while True:
            event, values = self.window.read()

            if event in (WIN_CLOSED,'-Back-'):
                self.window.close()
                self.menu.unhide_window()
                break

            elif event == '-Bar-':
                self.hide_window()
                init_Tela_CLLB(self)
            
            elif event == '-Salão-':
                self.hide_window()
                init_Tela_CLLS(self)

            elif event == 'Cozinha de Apoio':
                self.hide_window()
                init_Tela_CLLC(self)
    
    def close_window(self):
        if self.window is not None:
            self.window.Close()
    
    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()