from CLO.cl_operacao import  view
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

class Menu_CLO:
    def __init__(self):
        self.window = None

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
    
    def close_window(self):
        if self.window is not None:
            self.window.Close()
    
    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self):
        if self.window is not None:
            self.window.UnHide()