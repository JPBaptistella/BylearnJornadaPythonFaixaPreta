import PySimpleGUI as sg

def get_layout():
    frame_turno = [    
        [
            sg.Button(
                'Manhã',
                key='-Manhã-')
        ],

        [
        sg.Button(
            'Noite',
            key='-Noite-')
        ],
    ]

    layout =[
        [
            sg.Text('CheckList Operação')
        ],
        [
            sg.Frame(
                'Turno',
                frame_turno,
                )
        ],
        [
            sg.Button('Voltar'),
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