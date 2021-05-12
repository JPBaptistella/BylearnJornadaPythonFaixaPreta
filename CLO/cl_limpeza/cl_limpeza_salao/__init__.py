from CLO.cl_limpeza.cl_limpeza_salao import view
import PySimpleGUI as sg 
from PySimpleGUI import WIN_CLOSED


class Tela_CLLS:
    def __init__(self, Menu_CLL):
        self.window = None
        self.MenuL = Menu_CLL

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()
    
    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()
            
            if event in (WIN_CLOSED,'-Back-'):
                self.window.close()
                self.MenuL.unhide_window()
                break
    
    def close_window(self):
        if self.window is not None:
            self.window.Close()

    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()
    

    
