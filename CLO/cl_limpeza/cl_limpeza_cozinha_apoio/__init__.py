from CLO.cl_limpeza.cl_limpeza_cozinha_apoio import view
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

class Tela_CLLC:
    def __init__(self):
        self.window = None
    
    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
            self.instantiate()

            while True:
                event, values = self.window.read()

                if event == WIN_CLOSED:
                    self.close_window()
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