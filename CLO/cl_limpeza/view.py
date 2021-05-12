import PySimpleGUI as sg

def get_layout():
    frame_area =[
        [
            sg.Button(
                'Salão',
                key='-Salão-',
            )
        ],

        [
            sg.Button(
                'Bar',
                key='-Bar-',
            )
        ],

        [
            sg.Button(
                'Cozinha de Apoio',
                key='Cozinha de Apoio',
            )
        ],
    ]

    layout = [
        [
            sg.Text('CheckLists de Limpeza')
        ],
        [
            sg.Frame(
                'Áreas',
                frame_area,
            )
        ],
        [
            sg.Button(
                'Voltar',
                key='-Back-',
            ),
            sg.Button(
                'CheckList Operação',
                key='-CLO-'),
        ],
    ]
    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'CheckList Limpeza',
        get_layout(),
    )