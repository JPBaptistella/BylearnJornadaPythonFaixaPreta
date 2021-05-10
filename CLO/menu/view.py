import PySimpleGUI as sg

def get_layout():
    
    frame_header =[

        [
        sg.Text('Selina')
        ],

        [
         sg.Button(
                'CheckList Operação',
                key='-Operação-',
                size=(10,1),
            )
        ],

        [
            sg.Button(
                'CheckList Limpeza',
                key='-Limpeza-',
                size=(10,1),
            )
        ],
    ]
    
    layout = [
        [
            sg.Frame('Menu',frame_header)
        ]
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'Menu',
        get_layout(),
    )

