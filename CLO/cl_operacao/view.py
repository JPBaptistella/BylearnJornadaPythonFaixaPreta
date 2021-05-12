import PySimpleGUI as sg

def get_layout():
    frame_turno = [    
        [
            sg.Button(
                'Manhã',
                key='-Manhã-'
                )
        ],

        [
        sg.Button(
            'Noite',
            key='-Noite-')
        ],
    ]

    layout =[
        [
            sg.Text('CheckLists das Operações')
        ],
        [
            sg.Frame(
                'Turno',
                frame_turno,
                )
        ],
        [
            sg.Button(
                'Voltar',
                key='-Back-',
            ),
            sg.Button(
                'CheckList Limpeza',
                key='-CLL-'),
        ],
    ]
    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'CheckList Operação',
        get_layout(),
    )