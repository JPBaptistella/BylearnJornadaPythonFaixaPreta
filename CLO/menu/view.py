import PySimpleGUI as sg
from CLO.utils import inner_element_space

def get_layout():
    menu =[
            [
            sg.Text(
                'Selina',
                )
            ],

            [
            sg.Button(
                    'CheckList Operação',
                    key='-Operação-',
                    size=(20,1),
                )
            ],

            [
                sg.Button(
                    'CheckList Limpeza',
                    key='-Limpeza-',
                    size=(20,1),
                )
            ],
        ]
        
    layout = [
        [
            menu
        ],
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'Menu',
        get_layout(),
    )

